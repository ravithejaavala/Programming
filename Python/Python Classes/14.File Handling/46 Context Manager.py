# 22-04-25
'''
Context Manager:
----------------------
The usage of resources like file operations or data base connections is very common.
But these resources are limited in suply..In python,it can be achived by usage of
context managers which facilitate the proper handling of resources. The most common
way of performing file operations is by using the keyword 'with'

creating a context manager:
------------------------

When creating context managers using clases, user need to ensure that the class has
the methods:
_enter_() : It returns the resource that needs to be managed and

_exit_() : It does not return anything but performs the clean up opertions...

'''

# example of context manager

class ContextManager:

    def _init_(self):
        print('init method called')

    def _enter_(self):
        print('enter method called')

    def _exit_(self, exc_type, exc_val, exc_tb):
        print('exit method called')
with ContextManager() as obj:
    print('with statement')

# example
class File:
    def _init_(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    def _enter_(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def _exit_(self, exc_type, exc_val, exc_tb):
        self.file.close()
with File('test.txt','w') as fil_wr:
    fil_wr.write('hello')



'''
UI      BD      DB

html    java      mysql
css     python     postgres
js                  mongodb
an
react


json:

{}

json.dumps() : This method converts a python object(like a dictionary or list) into
a json formatted string. It takes a python object as an argument and returns a string
representation of the object in json format.

json.loads() : This method parses a json string and converts it into a python object
(usually a dict or list). It takes a json string as an argument and returns the corresponding
python object...


database:
mysql
posgres
monogdb...

'''

# postgres - psycopg2

import psycopg2

DB_NAME = 'postgres'
DB_USER = 'postgres'
DB_PASS = 'Password'
DB_HOST = 'localhost'
DB_PORT = '5432'

try:
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS,
                            host=DB_HOST, port = DB_PORT)
    print('database connected successfully')
except:
    print('database not connected successfully')