'''

Nested functions:
----------------
A function that is defined inside another function is know as inner function or nested function.
Nested functions can access variables of the enclosing scope...

syntax:
----

def fun1():
    # block of code

    def fun2():
        # block of code


Note:
---
If we are declaring the variables under the main function then you are able to access in the
nested function, but the variables which are defined in the nested function we are not able
to access in the main function...

'''


def fun1():
    text = 'In the main function'
    name = 'sarath'
    print(text)
    def fun2():
        print('--nested function--')
        print(name)
        def fun3():
            print('--inner function--')
            age = 30
            print(age)
        fun3()
    fun2()
fun1()


'''
lambda functions/anonymous functions:
-------------------------------------

Python lambda functions are anonymous functions means that the function is without a name.
As we already know the def keyword is used to define a normal function. Similarly, the lambda
keyword is used to define an anonymous functions..


syntax:
-----

lambda arguments:expession

'''


def squa(a):
    return a**2
res = squa(2)
print(res)


squ = lambda a:a**2
print(squ(3))


# example 2


element = lambda x : 'Even' if  x % 2 == 0 else 'Odd'

print(element(2))


'''
*Use of Microservices and where we are using it??**

Recursive functions:
----------------------
Recursion in python refers to when a function calls itself. There are many instances
when you have to build a recursive function to solve the Mathematical or recursive problems.


'''


def fact(n):

    if n == 0:
        return 1
    else:
        return n * fact(n-1)
print(fact(3))

print(fact(0))


'''
Local and global variables:
---------------------------

Local variables:
--------------
Variable declared inside a function body is know as "Local variable". These  have a local 
access  thus the variables can't be accessed outside of the function body in which they are
declared...


Global variables:
-------------------
These are the variables which are defined outside any function and which are accessible
throughout the program i.e , inside and outside of every function...

*global* keyword

'''

def dis():
    name = 'hyma' # local variable
    age = 28 # local variables
    print(name)
    print(age)
dis()


def wish():
    global msg
    msg = 'hello all'
    print(txt)
    print(msg)
txt = 'python programing' # global variable
wish()
print(txt)

print(msg)