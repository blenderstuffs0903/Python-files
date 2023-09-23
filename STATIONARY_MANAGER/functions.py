import mysql.connector as ms
from prettytable import PrettyTable
from datetime import datetime


def get_pswrd():
    password = input('Enter your mysql server password: ')
    return password


mydb = ms.connect(host='localhost', user='root', password=get_pswrd(), database='stationary_manager')
my_cursor = mydb.cursor()
user_atr = ('UserId', 'Username', 'FirstLogged-in', 'LastLogged-in')
item_atr = ('ItemNo', 'Item_name', 'Stock', 'price(in Rs)', 'Added_On')


def table_display(row, atr=item_atr):
    """Displays tubular data in ASCII table format"""
    table = PrettyTable()
    table.field_names = atr
    table.add_rows(row)
    return table


def display_items(query='select * from items', atr=item_atr):
    my_cursor.execute(query)
    rows = my_cursor.fetchall()
    if len(rows) == 0:
        return rows

    return table_display(rows, atr)


def search():
    # select search method
    print('''Enter 1 to search by Item Name
Enter 2 to search by price
Enter 3 to search by date added''')
    choice = input()
    if choice == '1':
        item_name = input('Enter the product name\n')
        query = f'select * from items where Item_name="{item_name}"'
        output = display_items(query)
        if type(output) is list:
            return f"No item named '{item_name}' is available"
        else:
            return output
    elif choice == '2':
        print('''Enter 1 to enter a specific price
Enter 2 to enter price range''')
        choice = int(input())
        if choice == 1:
            price = input('Enter the price\n')
            query = f'select * from items where price = {price}'
            output = display_items(query)
            if type(output) is list:
                return f'No items of price {price}'
            else:
                return display_items(query)
        elif choice == 2:
            min_price = input("Enter starting price\n")
            max_price = input("Enter max price\n")
            query = f'select * from items where price>={min_price} and price<={max_price}'
            return display_items(query)
    elif choice == '3':
        print('''Enter 1 to search items added on a day
Enter 2 to search items added on range of days''')
        date_method = int(input())
        if date_method == 1:
            year = int(input('Enter year: '))
            month = int(input('Enter month: '))
            date = int(input('Enter date: '))
            date2 = datetime(year, month, date + 1)
            date = datetime(year, month, date)
            output = display_items(f'select * from items where added_on > "{date}" and added_on < "{date2}"')

        elif date_method == 2:
            year_1 = int(input('Enter year_1: '))
            month_1 = int(input('Enter month_1: '))
            date_1 = int(input('Enter date_1: '))
            year_2 = int(input('Enter year_2: '))
            month_2 = int(input('Enter month_2: '))
            date_2 = int(input('Enter date_2: '))
            date1 = datetime(year_1, month_1, date_1)
            date2 = datetime(year_2, month_2, date_2+1)
            output = display_items(f'select * from items where added_on > "{date1}" and added_on < "{date2}"')

        if type(output) is list:
            return f"No items found..."
        else:
            return output


def add_items():
    items = int(input('How many items you want to add?\n'))
    val = []
    item_names = []
    modification = False
    for n in range(items):
        modification = False
        if items > 1:
            print(f'Enter item {n+1}')
        else:
            print('Enter Item-Name')
        item_name = input()
        if item_name.lower() in eval((str(get_column(column_no=2)).lower())):
            print(f'{item_name} already exists. Do you want to update instead? Enter "y" or "n"')
            to_update = input()
            if to_update == 'y':
                modify(item_name)
            modification = True
        else:
            stock = int(input('Enter stock\n'))
            price = float(input('Enter the price\n'))
            val.append((item_name, stock, price))
            item_names.append(item_name)
    if modification is False:
        query = 'insert into items(Item_name, stock, price) values(%s, %s, %s)'
        my_cursor.executemany(query, val)
        mydb.commit()
        if len(item_names) == 1:
            item_names = f'("{item_names[0]}")'
        else:
            item_names = tuple(item_names)
        print('The following items were added.')
        print(display_items(f'select * from items where item_name in {item_names}'))


def modify(item_name=None):
    to_continue1 = True
    is_modified = False
    while to_continue1:
        if item_name is None:
            item_name = input('Enter the item name you want to modify\n')
        else:
            print(f'Updating {item_name}...\n')
        if item_name.lower() not in eval(str(get_column(column_no=2)).lower()):
            print(f'No item named {item_name} was found')
            print("Do you want to add items? Enter 'y' or 'n'")
            choice = input()
            if choice == 'y':
                add_items()
                break
            else:
                break
        to_continue2 = True
        while to_continue2:
            print(display_items(f'select * from items where item_name="{item_name}"'))
            print('''=>Enter 1 to change the price
=>Enter 2 to add to stock
=>Enter 3 to remove from stock''')
            choice = int(input())
            if choice == 1:
                new_price = input('Enter new price in Rs\n')
                my_cursor.execute(f'update items set price={new_price} where item_name="{item_name}"')
                is_modified = True
            elif choice == 2:
                add_stock = int(input('Enter the number of new items you are adding\n'))
                old_stock = get_column('items', 3, item_name)
                stock = old_stock[0] + add_stock
                my_cursor.execute(f'update items set stock={stock} where item_name = "{item_name}"')
                is_modified = True
            elif choice == 3:
                old_stock = get_column('items', 3, item_name)
                if old_stock[0] == 0:
                    print('This item is out of stock')
                elif old_stock[0] != 0:
                    sub_stock = int(input('Enter the number of items to be removed: '))
                    if old_stock[0] < sub_stock:
                        stock = 0
                        my_cursor.execute(f'update items set stock={stock} where item_name = "{item_name}"')
                    else:
                        stock = old_stock[0] - sub_stock
                        my_cursor.execute(f'update items set stock={stock} where item_name = "{item_name}"')
                    is_modified = True

            if is_modified:
                print("Modification done successfully...")
                print(display_items(f'select * from items where Item_name="{item_name}"'), '\n\n')

            mydb.commit()
            print(f'Do you want continue modifying the item "{item_name}"? Enter "y" or "n".')
            to_continue = input().lower()
            if to_continue == 'n':
                to_continue2 = False
        print(f'Do you want modifications to other items? enter "y" or "n"')
        to_continue = input().lower()
        if to_continue == 'n':
            to_continue1 = False


def remove():
    item_name = input("Enter the item name to be removed\n")
    print('The following item was deleted...')
    print(display_items(f'select * from items where item_name="{item_name}"'))
    my_cursor.execute(f'delete from items where item_name="{item_name}"')


def get_column(table_name='items', column_no=1, item_name=None):
    """Returns the list of values of the passed column"""
    if item_name is not None:
        my_cursor.execute(f'select * from {table_name} where item_name = "{item_name}"')
    else:
        my_cursor.execute(f'select * from {table_name}')
    column = []
    for row in my_cursor:
        column.append(row[column_no-1])
    return column


def see_users():
    my_cursor.execute('select * from users')
    rows = my_cursor.fetchall()
    return table_display(rows, user_atr)


def search_user():
    username = input('Enter username: ')
    my_cursor.execute(f'select * from users where username="{username}"')
    users = my_cursor.fetchall()
    if len(users) > 0:
        return table_display(users, user_atr)
    else:
        return f'No user named "{username}" was found...'


def change_username():
    old_name = input('Enter the username you want to change: ')
    if old_name.lower() in eval(str(get_column('users', 2, )).lower()):

        new_name = input('Enter the new username: ').title()
        my_cursor.execute(f'update users set username = "{new_name}" where username = "{old_name}"')
        print(display_items(f'select * from users where username="{new_name}"', user_atr))
        mydb.commit()
    else:
        print(f'No user named "{old_name}" was found...')


def delete_users():
    username = input('Enter the username you want to delete: ')
    if username.lower() in eval(str(get_column('users', 2, )).lower()):
        print('Following user was deleted...')
        print(display_items(f'select * from users where username="{username}"', user_atr))
        my_cursor.execute(f'delete from users where username="{username}"')
        mydb.commit()
    else:
        print(f'No user named "{username}" was found...')


def sign_up():
    print('Looks like you are new, please login\n')
    name_valid = False
    full_name = ''
    while not name_valid:
        f_name = input('Enter your first name\n').capitalize()
        l_name = input('Enter your last name\n').capitalize()
        full_name = f'{f_name} {l_name}'
        if full_name in get_column('users', 2):
            print('Username already exists!')
        else:
            name_valid = True
    no_of_users = len(get_column('users'))
    if no_of_users == 0:
        user_id = 1
    else:
        user_id = no_of_users+1
    print(f'Your user id is {user_id}')

    q = 'insert into users(UserId, UserName) values(%s, %s)'
    val = (user_id, full_name)
    my_cursor.execute(q, val)
    mydb.commit()
    print(f'signed_in successfully! Welcome {full_name}')
    return full_name


def log_in():
    user = input('Enter your username\n').title()
    while True:
        if user in get_column('users', 2):
            print(f'Hello {user}')
            return user
        else:
            sign_up()
            break


def log_out(username):
    my_cursor.execute(f'update users set Last_Logged_in=current_timestamp() where username = "{username}"')
    mydb.commit()


def close(username):
    log_out(username)
    mydb.close()
