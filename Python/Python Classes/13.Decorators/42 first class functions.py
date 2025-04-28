# 15-04-25
'''

API: C R U D
---

Create - post ****

Retriev - get

Update - put

Delete - delete


url
method
payload

We need to authenticate the API ----

Bearer token
o auth
o auth 2
jwt



Decorators:
---------
In python, decorators are a powerful mechanism to modify or extend the behvaiour
of a function or method without directly aletring the original code...

It essentially wrap a function with another function, adding the funcationality before
and after the function...

3 things are required:
----
first class functions or objects
nested functions
wrapper functions


how to call the decorator?

@decorator_name

first class functions:
---------------------
In python , functions are first class functions , which means:
    1. we can assign a function to a variable
    2. we can pass a function as an argument to another function
    3. We can return a function from another function


'''


# first class functions

def shout(txt):
    return txt.upper()

# assiging a function a variable
speak = shout
print(speak('sarath'))


def greet(func):
    msg = func("hello")
    print(msg)
greet(shout)


'''
nested functions:
---------------
A function can be defined one more function then we can call it as a nested function...


syntax:
----
def main():
    pass
    def inner():
        pass

'''

# nested functions

def main():
    print('--main function--')
    def inner():
        print('--inner function--')
    inner()
main()


# nested functions - 2


def parent():
    print('parent function')

    def child1():
        print('child1 function')

    def child2():
        print('child2 function')

    child1()
    child2()
parent()