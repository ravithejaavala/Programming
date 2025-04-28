# 12-03-25


# previous class start----------------
'''
Functions:
----------

Python functions is a block of code or block of statements that return the specific task..
The idea is to put some commonly or repeatedly done task together and make a function so that
instead of writing the same code again and again for different inputs, we can do the function calls
to reuse code contained in it over and over again..


Benefits:
----
Increase the Code Readability
Increase the Code Reusability..


Function Declaration:
--------------
def function_name(parameters):
    # body of the function

function_name(arguments) -- calling the function




'''
# previous class end-------------------------
'''

Functions:
----------

A function is a self block of code which is used to organize the functional code...
Function can be called as a section of program that is written once and can be executed
whenever required in the program, it make code reusability...

def function_name(parameters):
    # block of code
function_name(arguments) -- calling function

** calling function should be mandotory because the function execution basically starts at function call


Types of Function:
--------------------
There are two types of functions:
1. Built in function       : These are Standard functions in python that are available to use
    print(), len(), list(), tuple(), dict(), set(),....

2. User defined function: We can create our own functions based on our requirements

'''

def sample(): # sample - function name
    print('hello all') # body of the function
sample() # calling function


def add(a,b,c): # a,b,c - parameters
    res = a+b+c # body of the function
    print(res)
add(1,2,3) # calling the function & 1,2,3 - arguments
add(2,2,6)

add(1,1,1)

# def last_name()
'''
return statement:*****************
--------------- 

A return statement is used to end the execution of the function call and it "returns" the
value of the expression following the return keyword to the caller.
The statements after the return statements are not executed. If the return statement is without
any expression, then the special value None is returned.

'''


def addition(a,b):
    print('block of code')
    return a+b

print(addition(1,2))


'''
1. Without parameter without return type
2. with parameter without return type
3. without parameter and with return type
4. with parameter and with return type

'''

# 1. Without parameters and without return type


def wish():
    print('hello world!!')
wish()


# 2. with parameters without return type

def add(a,b): # a,b are the parameters
    res = a+b
    print(res)
add(1,22) # 1,22 - arguments

# 3. without parameter and with return type

def mul():
    a = 2
    b = 3
    return a*b
print(mul())


# 4. with parameter and with return type *************** 95%

def details(name, age, gender):
    return name, age, gender
print(details('dinesh kumar',23,'male'))
print(details('hyma',29,'female'))