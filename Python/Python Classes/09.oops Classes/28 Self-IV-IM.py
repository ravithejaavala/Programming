# 20-03-25
'''

self in python:
--------------


The self represents the instance of the class being used. Whenever we create an object from
a class, self refers to the current object instance. It is essential for accessing attributes
and methods within the class...

Instance variables - Instance Method : self  --- 90%

Class variable - Class method : cls

Static variable - Static method : there is no first parameter


Emp_ID   Emp_Name    Emp_office_loc     Emp_age

IV          IV              CV              IV


Instance variable - Individual details

class variable - shareable and modifiable



Instance variable and Instance method:
--------------------------------------

Instance attributes are those attributes that are not shared by the objects. Every object
has it own copy of the instance attribute i.e.. for every object, instance attribute is
different. There are two different ways to access the instance variable of class:
    1. within the class by using the self() and object reference
    2. Using the getattr() method



'''

class Student(object):

    def _init_(self, name, age, gender, total_marks): # state/data member -- instance variables
        self.name = name # self.name -- instance variable & name -- variable
        self.age = age
        self.gender = gender
        self.total_marks = total_marks

    def student_details(self): # fields/methods --  instance method
        print(self.name, self.age, self.gender, self.total_marks)

bhanu = Student('bhanu',25,'male',550) # creation of an object
bhanu.student_details()

sai = Student('sai',28,'male',500) # creation of an object
sai.student_details()


# example - 2 : instance variable - instance methods

class Car:

    def _init_(p, color, model):
        p.color = color
        p.model = model

    def display(p):
        print(p.model, p.color)

audi = Car('grey',2025)
audi.display()