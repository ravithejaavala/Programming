# 26-03-25
'''
Inheritance:
-----------
Extracting the properties from one class to another class then we can call it as a inheritance

----or------
Extracting the properties that allows a child class or derived class to inherit attributes
and methods from another class (parent or base class).,....

Types of inheritance:
----------------
single inheritance       -- 90%
multi level inheritance
multiple inheritance
hierarchical inheritance


'''

class Emp: # parent class
    def _init_(self, name, age):
        self.age = age
        self.name = name

    def display(self):
        print(self.name, self.age)

class GovtEmp(Emp): # GovtEmp class is a child class

    def _init_(self, name, age, gender):
        self.gender = gender
        Emp._init_(self, name, age) # invoking the super class or parent class

    def wish(self):
        print(self.name, self.age, self.gender)

ravi = GovtEmp('ravi',26,'male') # creating an object for the child class
ravi.display()
ravi.wish()

'''

Invoking the super class:
------
there are two ways to access the super class or parent class details into the child class
    1. with the help of Parent class name
    2. with the help of super() (builtin function)

'''
# super()
class Person:

    def _init_(self, id, name):
        self.id = id
        self.name = name

    def dis(self):
        print(self.id, self.name)


class Employee(Person):

    def _init_(self, id, name, sal):
        self.sal = sal
        super()._init_(id, name) # invoking the super class with the help of super()

    def dis(self):
        print(self.id, self.name, self.sal)

sai = Employee(123,'sai',3456788)
sai.dis()


'''
single inheritance :
------------------

Single inheritance enables a derived class to inherit properties from a single parent
class, thus enabiling code reusability and the addition of new features to existing
code.....

class A:
|
|
|
class B(A):
|
|
|
'''

# single inheritance

class Parent: # base class or parent class

    def _init_(self, id, name, gender):
        self.id = id
        self.name = name
        self.gender = gender

    def dis(self):
        print('--In the parent class method---')

class Child(Parent): # child class or derived class

    def _init_(self, id, name, gender, sal):
        self.sal = sal
        # Parent._init_(self, id, name, gender, sal)
        super()._init_(id, name, gender) # invoking the super class

    def wis(self):
        print('--In the child class method---')
        print(self.id, self.name, self.gender, self.sal)
dinesh = Child(1234,'dinesh','male',23456) # creating the object for child class
dinesh.wis()
dinesh.dis()


sarath = Parent(456,'sarath','male')
# sarath.wis()
sarath.dis()

#-------------------------------------------------------------------------------------------
# For Private Members

class Parent: # base class or parent class

    def _init_(self, id, name, gender):
        self.id = id
        self.name = name
        self.gender = gender

    def dis(self):
        print('--In the parent class method---')

class Child(Parent): # child class or derived class

    def _init_(self, id, name, gender, sal):
        self.sal = sal
        # Parent._init_(self, id, name, gender, sal)
        super()._init_(id, name, gender) # invoking the super class

    def wis(self):
        print('--In the child class method---')
        print(self.id, self.name, self.gender, self.sal)
dinesh = Child(1234,'dinesh','male',23456) # creating the object for child class
dinesh.wis()
dinesh.dis()


sarath = Parent(456,'sarath','male')
# sarath.wis()
sarath.dis()

