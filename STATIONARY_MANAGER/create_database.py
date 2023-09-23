import pickle
import mysql.connector as ms

pswrd = input('Enter your mysql server password: ')

mydb = ms.connect(host='localhost', user='root', password=pswrd)
my_cursor = mydb.cursor()
file = open('rows.bin', 'rb')
table_rows = pickle.load(file)

my_cursor.execute(f'Create database stationary_manager')
my_cursor.execute('use stationary_manager')
my_cursor.execute('create table items(ItemNo int primary key Auto_increment,'
                  'Item_name varchar(30),'
                  'Stock int,price float(10, 2),'
                  'Added_On timestamp default current_timestamp)')
my_cursor.execute('create table users(UserId int primary key,'
                  'UserName varchar(30),'
                  'First_Logged_in timestamp default current_timestamp(),'
                  'Last_Logged_in timestamp default current_timestamp())')

query = 'insert into items values(%s, %s, %s, %s, %s)'
my_cursor.executemany(query, table_rows)
mydb.commit()
print('Database imported successfully!')


file.close()
