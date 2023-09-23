# import mysql.connector as ms
# from prettytable import PrettyTable
# mydb = ms.connect(host='localhost', user='root', password='DORACHAN', database='stationary_manager')
# my_cursor = mydb.cursor()
#
#
# def get_column(cursor):
#     """Returns the list of values of a column from desc table query output"""
#     attributes = []
#     for row in cursor:
#         attributes.append(row[0])
#     return attributes
#
#
# my_cursor.execute("desc users")
# obj = my_cursor.fetchall()
# user_atr = get_column(obj)
#
# print(user_atr)
#
# my_cursor.execute("desc items")
# obj = my_cursor.fetchall()
# item_atr = get_column(obj)
#
# print(item_atr)
import mysql.connector as ms
from prettytable import PrettyTable
user_atr = ['UserNo', 'UserName', 'FirstLogged', 'LastLogged', 'Password']
item_atr = ['ItemNo', 'Item_name', 'Stock']


def get_column(table_name, column_no=1):
    """Returns the list of values of a column from desc table query output"""
    my_cursor.execute(f'select * from {table_name}')
    column = []
    for row in my_cursor:
        column.append(row[column_no-1])
    return column


user = input('Enter you name\n')

if user in get_column('users', 2):
    print(f'Hello {user}')
else:
    print('Looks like you are new, please login')
