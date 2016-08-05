import sqlite3

conn = sqlite3.connect('D:\\Workspace\\flaskr\\tmp\\flaskr.db')
cursor = conn.cursor()
# cursor.execute('drop table if exists user')
# cursor.execute(
#     'create table user (id varchar(20) primary key, name varchar(20))')
# cursor.execute('insert into user (id,name) values (\'1\',\'Amy\')')
# print cursor.rowcount

cursor.execute('select columns from entries')
values = cursor.fetchall()
print values
cursor.close()
conn.close()
