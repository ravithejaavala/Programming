'''

Exception handling:
-------------------

Exception handling handles error that occur during the execution of the program..
Exception handling allows to respond to the error, instead of crashing/stopping the
application or program... So it enables you to catch and manage the errors, making your
code more robust and user friendly...


try:  The code which may causes an exception/error

except: To handles the exception

else: If there is no exception then only else block will execute

finally: For closing the database operations


1. error   - syntax error
2. exception  - ZeroDivisionError, AttributeError, TypeError, ValueError.....




'''

# sample of exception handling

# m = 9
# n = 0
# print(m/n)

# ZeroDivisionError

print('bhanu')


'''
                Exception

ZeroDivisionError   TypeError       KeyError


'''


try:
    m = 9
    n = 0
    print(m / n)
except ZeroDivisionError as zde:
    print(zde)

'''
1. If we are writing the try block , the except block is mandatory...

2. If we are writing the else block , the except block is mandatory

'''

try:
    name = 'hyma'
    age = 28
    print(name+age)
except Exception as er:
    print(er)
else:
    print('--in the else block---')
finally:
    print('closing')


# multiple except block

def divide(x,y):
    try:
        res = x/y
    except ZeroDivisionError as zde:
        print('----------',zde)
        print(zde)
    except TypeError as te:
        print('----------', te)
        print(te)
    else:
        print(res)
    finally:
        print('completed')
print(divide(2,'a'))


'''

Exceptions are 2 types:

built in exception  -- Exception, ValueError............
user defined exception : *raise* with the help of raise keyword , we will raise the exceptions

'''

# example for user defined exception


def div(a,b):

    if b == 0:
        raise ZeroDivisionError('the denominator number should not be zero at any cost')
    return a/b

res = div(1,2)
print(res)
try:
    res = div(1,0)
    print(res)
except ZeroDivisionError as e:
    print(e)


# example - 2 for user defined exceptions

def wish(val):

    if val > 100:
        raise ValueError(f"value {val} is too large and we are accepting below 100")
    else:
        print(f'value {val} is acceptable range')
try:

    res = wish(10)
    print(res)
except ValueError as e:
    print(e)


'''
nested exception handling

'''