# 04-04-25
'''

Exception handling:
------------------
Exception handling is a crucial mechanism for dealing with errors that occur during the
execution of the program...

TypeError
ValueError
AttributeError...................

Exception are two types:
-----------------
syntax error
exceptions


syntax error:
-----------
While writing the code if we are not providing the proper indentation and if we are not
writing the standard of code(pep8) then it will raise a syntax error..


exceptions:
------------
Exceptions are used to handle the exception and without stopping the flow of the execution
so however, it changes the output..

How we can handle the exception?

try

except

else

finally


'''

a = 9
if a>4:
    print(True)


# exception handling

try:
    name = 'sarath'
    n = 9
    print(name + n)
except TypeError as err:
    print(err)


print('hyma sree')


'''

try   : the code which may causes an exception/error

except : handles the exeception

else : if there is no execption then else part will execute

finally : finally is an optinal and it will execute all the time and we will the close the DB operation


'''

try:
    a = 9
    b = 0
    print(a / b)
except ZeroDivisionError as er:
    print(er)
else:
    print('in the else block')
finally:
    print('finally block')

# example - 2


try:
    name = 'sarath'
    last_name = 'k'
    print(last_name + name)

except Exception as e:
    print(e)
else:
    print('---In the else block----')
finally:
    print('--finally block--')

'''
SC-1:
----

if exception occurs:

1. If the exception occures at line 3 in try block
2. Python interpreter stops the executing the remaining statements
3. It will goes to the execpt block and it executes the except block
4. Since in the try block exception got raised it won't execute the else block
5. And it executes finally block statement

SC-2:
----
if no exception occurs:

1. Python executes all the statements in the try block
2. It won't execute the except block
3. It will execute the else block statement
4. finally it will execute the finally block



'''