# 02-04-25

"""
*args , **kwargs can pass a variable 'n' number of arguments to a function using the special
symbols.

*args     - Non - keyword arguments
**kwargs  - keyword arguments
"""
'''

Polymorphism:
------------
The polymorphism is nothing but "too many formations" ...
It allows the entites like functions, methods or operators to behave differently based
on the type of data that are handling..


'''


li = [1,2,3]

str = 'hyma'


print(len(li))

print(len(str))


# polymorphism in operators

print(10+10)


# function in polymorphism


def add(a,b):

    return a+b

print(add(1,2))

print(add('k',' sarath'))

'''
method overloading
method overiding

method overloading:
-------------------
Two or more methods have the same name but different numbers of paramters or different
types of parameters. These methods are called overloaded and this is nothing but
method overloading....

In generaly python does not support method overloading by default. But there are different
ways to achieve method overloading in python...


'''

def addition(a,b):
    res = a+b
    print(res)

def addition(a, b,c):
    res = a + b + c
    print(res)

addition(1,2,3)


# another way to achive method overloading

def addition1(datatype, *args):

    if datatype == 'int':
        ans = 0

    if datatype == 'str':
        ans = ''

    for i in args:
        ans = ans+i
    print(ans)
addition1('int',1,2)
addition1('int',2,2,2)
addition1('str', 'dinesh',' b')



'''

Method overriding:
-----------------
Method overiding is an ability of any object oriented programming language that allows
a sub class or child class to provide a specific implementation of a method that is already
provided by one of its super class or parent classes. When a method in a sub class has
the same name, same parameters and same return type as a method in its super class,
then the sub class is said to be override the method in the super class...


'''

class Parent:

    def _init_(self):
        self.value = 'Inside the parent'

    def show(self):
        print(self.value)

class Child(Parent):

    def _init_(self):
        self.value = 'Inside the child'

    def show(self):
        print(self.value)

obj1 = Parent()
obj2 = Child()

obj1.show()
obj2.show()


# method overriding in multiple inheritance

class Parent1:

    def show(self):
        print('Inside the parent - 1 class')

class Parent2:

    def dis(self):
        print('Inside the parent-2 class')

class Child(Parent1, Parent2):

    def show(self):
        print('Inside the child class')

obj = Child()
obj.show()
obj.dis()


'''
operator overloading:
--------------------
In python, operator overloading is also know as polymorphism, allows you to customize
the behaviour of standard operators like (+,-,*...) for your own classes...


'''


class Addition:

    def _init_(self, x,y):
        self.x = x
        self.y = y

    def _add_(self, other):
        return Addition(self.x + other.x, self.y + other.y)

    def _str_(self):
        return f'{self.x},{self.y}'


obj = Addition(1,2)
obj1 = Addition(3,4)

res = obj+obj1
print(res)