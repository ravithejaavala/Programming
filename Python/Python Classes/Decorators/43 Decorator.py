# 18-04-25
'''

Decorators:
-----------
In python, decorators are a powerful and flexible way to modify or extend the behaviour of a function or methods,
without chaning their actual code... A decorator is essentially a function that takes another function as an argument
and returns a new function ....

Decorators are often used in scenarios such as logging, authentication and memorization...allowing us to add the
functionality to existing functions or methods to clean and reusable...



First class functions or objects
nested functions
wrapper functions

First class functions or objects:
-----------------------------------

First class functions can pass an argument to the another function...
the first class functions can be treated like any other object, such as int,
string, list... This gives function a unique level of flexibilty and allows them
to passed arouned and manupulated....

'''

# first class function

# assiging a function to a variable

def dis(n):
    return f'Hello {n}!!!'
res = dis
print(res('sarath'))

# passing a function as an argument

def wish(func, v):
    return func(v)
obj = wish(res, 'dinesh')
print(obj)

# nested function and returning function

def display(f): # main function
    def multiply(x): # inner function/nested function..
        return x * f
    return  multiply
mul = display(2) # f - parameter
print(mul(3)) # x - parameter


'''
first class functions
nested functions
returing/wrapper functions


@decorator
'''

# decorator
# 1. function decorators

def decorator(func):
    def wrapper():
        print("before calling the function")
        func()
        print('after calling the function')
    return wrapper

@decorator
def wish():
    print('hello all')
wish()

# 2.method decorators

def method_decorator(func):
    def wrapper(self, *args, **kwargs):
        print('Before method execution')
        res = func(self, *args, **kwargs)
        print('after method execution')
        return res
    return wrapper

class Decorator:
    @method_decorator
    def dis(self):
        print('hi!!!')
obj = Decorator()
obj.dis()


# square the list of elements by using the decorator

def squ_decorator(func):
    def inner(numbers):
        res = [i**2 for i in func(numbers)]
        return res
    return inner

@squ_decorator
def squ(li):
    return li
li = [1,2,3,4,5,6]
result = squ(li)
print(result)