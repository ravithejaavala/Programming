# 19-03-25
'''
OOPS:
----


Constructors:
------------

In python, a constructor is a special method that is called automatically when an object
is created from a class. It's main role is to *initialize* the object by setting up its attributes
or state or fields...

The _new_ is the constructor that creates a new instance of the class and while
_init_ is the initializer that sets up the instance's attributes after creation. These
methods work together to manage object creation adn initialization...


_new_ : ***********************

_new_ is a special method/dunder method and the responsible for creating a new instance
of the class.

'''


class Sample(object):

    def _new_(cls, *args, **kwargs):
        print('Creating instance or object')
        return super(Sample, cls)._new_(cls)

    def _init_(self):
        print('Initializing object')

Sample()


'''
Types of Constructors:
--------------------

Default Constructor
Parameterized Constructor

Default Constructor:
-------------------
A default constructor does not take any parameters other than self. It initializes the 
object with default attribute values



Parameterized Constructor:
-----------------------------

A parameterized constructor accepts arguments to initialize the object's attributes with
specific values..

'''


class Emp:

    def _init_(self):
        self.emp_name = 'hyma'
        self.emp_off_loc  = 'blr'
        self.sal = 3456234
    def get(self):
        print(self.emp_name, self.emp_off_loc, self.sal)

hyma = Emp() # while creating the object , internally the  _new_ method called and it will create an object in the memeory
hyma.get()




class Car:

    def _init_(self, car_name, model, color):
        self.car_name = car_name
        self.model = model
        self.color = color
    def get_car_details(self):
        print(self.car_name, self.model, self.color)
bmw = Car('bmw',2025, 'black')
bmw.get_car_details()