
import mysql.connector

def main():
    conn=mysql.connector.connect(host='127.0.0.1',user='root', password='yuliang',port=3306)
    cursor=conn.cursor()
    print(cursor)
    cursor.execute("create database if NOT EXISTS blog2017")
    cursor.execute('use blog2017')
    cursor.execute('create table if not exists user('
                   '_id int PRIMARY KEY auto_increment,'
                   '_name VARCHAR(20) UNIQUE not null,'
                   '_password VARCHAR(20) not null,'
                   '_github VARCHAR(20),'
                   '_wechat VARCHAR(20),'
                   '_info VARCHAR(200),'
                   '_access int not null)')
    print('create user table')

    cursor.execute('create table if not exists articles ('
                   '_id int PRIMARY KEY auto_increment,'
                   '_img text,'
                   '_subtitle text,'
                   '_class int,'
                   '_author text,'
                   '_create DATETIME,'
                   '_update DATETIME,'
                   '_counts int,'
                   '_title text,'
                   '_content text)')
    print('create articles table')

    cursor.execute('create table if not exists comment('
                   '_id int PRIMARY KEY auto_increment,'
                   '_content text,'
                   '_name text,'
                   '_create DATETIME,'
                   '_fatherid int,'
                   '_sonid int,'
                   '_for int)')
    print('create comment table')


    cursor.execute('create table if not exists album ('
                   '_id int PRIMARY KEY auto_increment,'
                   '_img text,'
                   '_content text,'
                   '_create DATETIME,'
                   '_update DATETIME,'
                   '_counts int,'
                   '_author text,'
                   '_class int)')

    print('create album table')

    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()
