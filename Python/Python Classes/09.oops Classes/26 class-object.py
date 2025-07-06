# 18-03-25

# previous class start -----------------

'''
OOPS:
------
OOPS stands for object oriented programming language , the developers maintable and scalablr
applications.
By understaning the core OOP principles (classes, object, inheritance, encapsulation..)
programmers can leverage the full potentail of python OOPS desing the elegant and efficient
solutions to complex problems

Every Application has two things:
    
    1. Class based API's   -- application having the standard
    2. Function based API's

    API : Application Programming Interface
    
    Request Method : POST, GET, PUT , DELETE
    
    Request URL : https://example.com
    
    Payload : 
    
    Example:
    ----
    Request URL: https://www.python.org/   (endpoint)
    
    Request Method: GET

'''
name = 'hyma' # object -- oops
print(name)
# previous class end-----------------



'''
OOPs:
------


OOPs is a way of organizing code that uses objects and classes to represent the real-world
entites and their behaviour. In OOPs, object has the attributes thing that has specific
data and it can perform certain actions using the methods

OOPs concepts in python:
---------------
class
object
polymorphism
encapsulation
inheritance
data abstraction
Operator overloading

Instance Variables - Instance Methods
Class Variables - Class Methods
Static Variables - Static Methods


class:
-----
A user defined prototype for an object that defines a set of attributes that characterize
any object of the class. So the attributes are:
    1. data members/Fields/state (class variables, instance variables, static variables)
    2. Methods/ behaviour          (class method, instance method, static method)


----OR----------

A class is a collection of objects. Classes are blueprints for creating objects. A class
defines a set of attributes and methods that the created objects(instances)...

A class is a blueprint for creating objects. It defines attributes (variables) 
and methods (functions) that describe the behavior of the objects created from the class.

class is logical structure 

Note:
----
classes are created by keyword class
attributes are the variables that belong to a class
While writing class name - the first character should be in the upper case
Class is a logical structure

# __init__  : special method/dunder method/ magic method  (__new__, )

Objects:
-----
An object is an instance of a class. It represents a specific implementation of the class
and holds its own data.
An object consists of:

State : It is represented by the attributes and reflects the properties of an object
Behaviour : It is represented by the methods of an object and reflects the response of an
            object to the other object


Constructor in Python (__init__ method)
--------------------------------------
A constructor is a special method in Python classes, named __init__, that is automatically 
called when an object is created. It initializes the object's attributes.

__new__ :- It is a constructor, that creates the new instance of a class   
          or Creates a new instance  i.e (memory allocation)
    ***whenever the object is created, internally the "__new__" 
    method is called and then an instance is created(memory is allocated)

__init__ :- Initializes the created instance

***super class is object

1. Default Constructor :- If no parameters are passed, the constructor can still define default values.

2. parameterized  :-  




'''

class Emp:

    def _init_(self, name, age): # state/data member
        self.name = name
        self.age = age

    def details(self): # methods
        print('name::',self.name, 'age::',self.age)

sarath = Emp('sarath',30) # object creation
sarath.details()


# Example - 2

class Student(object): # class

    def _init_(self, st_name, st_age):  # attributes : data members
        self.st_name = st_name
        self.st_age = st_age

    def st_details(self): # methods
        print(self.st_name, self.st_age)


dinesh = Student('dinesh',27) # object creation
dinesh.st_details() # with the help of object - calling the method