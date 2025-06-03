# 24-04-25


# previous class start-----------
'''
database:
mysql
posgres
monogdb...

'''
# postgres - psycopg2

import psycopg2

DB_NAME = 'postgres'
DB_USER = 'postgres'
DB_PASS = 'ravi'
DB_HOST = 'localhost'
DB_PORT = '5432'

try:
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS,
                            host=DB_HOST, port = DB_PORT)
    print('database connected successfully')
except:
    print('database not connected successfully')
# previous class end----------------------



'''
psycopg2:
--------

'''

# create a table

import psycopg2

DB_NAME = 'postgres'
DB_USER = 'postgres'
DB_PASS = 'Password'
DB_HOST = 'localhost'
DB_PORT = '5432'

try:
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port = DB_PORT)
    print('database connected successfully')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE Emplyoee(ID Int, emp_name TEXT NOT NULL, Email TEXT NOT NULL)""")
    conn.commit()
except:
    print('Database not connected')

# insert data into the table
DB_NAME = 'postgres'
DB_USER = 'postgres'
DB_PASS = 'Password'
DB_HOST = 'localhost'
DB_PORT = '5432'

try:
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port = DB_PORT)
    print('database connected successfully')
    cur = conn.cursor()
    cur.execute("""INSERT INTO Employe (ID, emp_name, Email) VALUES (1, sarath, sarath@gmail.com),
                                        (2,'hyma',hyma@gmail.com)""")
    conn.comit()
    conn.close()
except:
    print('Database not connected')


# fetch the data from the table
DB_NAME = 'postgres'
DB_USER = 'postgres'
DB_PASS = 'Password'
DB_HOST = 'localhost'
DB_PORT = '5432'

try:
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port = DB_PORT)
    print('database connected successfully')
    cur = conn.cursor()
    cur.execute("""select * from Employee""")
    data = cur.fetchall()
    # data = cur.fetchone()
    print(data)
except:
    print('Database not connected')

'''

datetime
time

'''
from datetime import *

now = datetime.now()
print(now)

print('date now:{}-{}-{}'.format(now.day, now.month, now.year))

# today's data and time

td = datetime.today()
print(td)

import calendar
from calendar import month

# calendar

yy = int(input("enter year"))
mm = int(input('enter month'))

str1 = month(yy,mm)
print(str1)

'''
     April 2025
Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6
 7  8  9 10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27
28 29 30
'''

yy = int(input("enter year"))

print(calendar.calendar(yy))


'''
January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
       1  2  3  4  5                      1  2                      1  2
 6  7  8  9 10 11 12       3  4  5  6  7  8  9       3  4  5  6  7  8  9
13 14 15 16 17 18 19      10 11 12 13 14 15 16      10 11 12 13 14 15 16
20 21 22 23 24 25 26      17 18 19 20 21 22 23      17 18 19 20 21 22 23
27 28 29 30 31            24 25 26 27 28            24 25 26 27 28 29 30
                                                    31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6                1  2  3  4                         1
 7  8  9 10 11 12 13       5  6  7  8  9 10 11       2  3  4  5  6  7  8
14 15 16 17 18 19 20      12 13 14 15 16 17 18       9 10 11 12 13 14 15
21 22 23 24 25 26 27      19 20 21 22 23 24 25      16 17 18 19 20 21 22
28 29 30                  26 27 28 29 30 31         23 24 25 26 27 28 29
                                                    30

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6                   1  2  3       1  2  3  4  5  6  7
 7  8  9 10 11 12 13       4  5  6  7  8  9 10       8  9 10 11 12 13 14
14 15 16 17 18 19 20      11 12 13 14 15 16 17      15 16 17 18 19 20 21
21 22 23 24 25 26 27      18 19 20 21 22 23 24      22 23 24 25 26 27 28
28 29 30 31               25 26 27 28 29 30 31      29 30

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
       1  2  3  4  5                      1  2       1  2  3  4  5  6  7
 6  7  8  9 10 11 12       3  4  5  6  7  8  9       8  9 10 11 12 13 14
13 14 15 16 17 18 19      10 11 12 13 14 15 16      15 16 17 18 19 20 21
20 21 22 23 24 25 26      17 18 19 20 21 22 23      22 23 24 25 26 27 28
27 28 29 30 31            24 25 26 27 28 29 30      29 30 31




Regular expression
multi threading

'''