# 03-04-25
'''
data abstraction:
---------------
Abstraction in python is a process of handling complexity by hiding the unnecessary details and
showing only the essential information to the user.. In generally, it is the one of the
core principles of oops which is allows developers to implement more complex functionality
without worrying about the underlying complexity...


Abstraction in Real world:

We can take as example for the social media platform (Facebook). the user is real intreseted
to send the messages, share photos... but he/she don't need to know the how to handles
data in background, managing the server....


Importance of abstraction:

Abstraction helps hide all the irrelevant data/process of an application to reduce the
complexity and increase the efficiency of the program....
So that it makes the code reusable and easier to read and allows for better maintentance...

While implementing the data abstraction class, atleast one abstract method it should be
there....

abstract method:
---------------
Before writing the abstract method we need to call decorator (@abstractmethod) and the
abstract method has the declaration but it does not have the implementation..

Note:
---
while working on the data abstraction, we must import the package which "abc" and make
the super class as 'abc'

** from abc import ABC, abstractmethod **

'''


from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Square(Shape):

    def _init_(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


class Rectangle(Shape):

    def _init_(self, l ,w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w
squ = Square(4)
print(squ.area())


reactangle = Rectangle(4,6)
print(reactangle.area())

'''
exception handling

'''