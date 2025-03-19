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
CLass is a logical structure

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
# =========================================================================================

# method --- a function that is associated with the class

# Here's a simple example to differentiate instance and class in Python:

# Class definition
class Car:
    wheels = 4  # Class variable (shared by all instances)

    def __init__(self, brand):
        self.brand = brand  # Instance variable (unique to each object)

# Creating instances (objects)
car1 = Car("Toyota")
car2 = Car("Honda")

# Accessing class variable
print(Car.wheels)   # Output: 4 (Accessed via class)
print(car1.wheels)  # Output: 4 (Accessed via instance)

# Accessing instance variable
print(car1.brand)   # Output: Toyota
print(car2.brand)   # Output: Honda

# Modifying class variable
Car.wheels = 6
print(car1.wheels)  # Output: 6
print(car2.wheels)  # Output: 6

# Modifying instance variable
car1.brand = "Ford"
print(car1.brand)   # Output: Ford
print(car2.brand)   # Output: Honda


"""
Key Difference
Class variable (wheels) → Shared across all instances. Changing it via the class changes it for all instances.
Instance variable (brand) → Unique to each object. Changing it affects only that particular instance."""


#                                                 # Instance and object


"""
Instance vs Object in Python
In Python, instance and object are closely related but have a slight difference in context:

Object
An object is a more general term that refers to any entity created from a class.
Everything in Python (like integers, strings, lists, etc.) is an object.
Instance
An instance is a specific object created from a particular class.
All instances are objects, but not all objects are instances of user-defined classes.
"""
#Example

# Class definition
class Dog:
    def __init__(self, name):
        self.name = name

# Creating instances (objects)
dog1 = Dog("Buddy")  # Instance of Dog class
dog2 = Dog("Charlie")  # Another instance of Dog class

# Checking types
print(isinstance(dog1, Dog))  # Output: True (dog1 is an instance of Dog)
print(isinstance(5, Dog))     # Output: False (5 is not an instance of Dog)
print(isinstance(5, int))     # Output: True (5 is an object, but not an instance of Dog)


"""
Key Difference
Object: A broader term — everything in Python is an object.
Instance: A specific object created from a particular class.
All instances are objects, but not all objects are instances of a user-defined class."""

#                                                 # Attribute 

"""
Attribute in Python
An attribute is a variable that belongs to a class or an instance. Attributes store data 
associated with an object or class.

Types of Attributes
Instance Attribute — Specific to each object (defined inside __init__).
Class Attribute — Shared across all instances (defined outside __init__).
"""
# Example

# Class definition
class Student:
    school = "ABC School"  # Class attribute (shared by all instances)

    def __init__(self, name, grade):
        self.name = name   # Instance attribute (unique to each object)
        self.grade = grade # Instance attribute (unique to each object)

# Creating instances
student1 = Student("Ravi", "A")
student2 = Student("Kiran", "B")

# Accessing attributes
print(student1.name)     # Output: Ravi (Instance attribute)
print(student2.grade)    # Output: B (Instance attribute)
print(student1.school)   # Output: ABC School (Class attribute)
print(student2.school)   # Output: ABC School (Class attribute)

# Modifying attributes
student1.grade = "A+"
print(student1.grade)    # Output: A+ (Only student1's grade changed)

Student.school = "XYZ School"  # Changing class attribute
print(student1.school)   # Output: XYZ School
print(student2.school)   # Output: XYZ School

"""
Key Points
Instance attributes → Defined inside __init__() and specific to each object.
Class attributes → Defined outside __init__() and shared among all instances.
Attributes are accessed using object.attribute or Class.attribute."""

#                                                 # What are present in attributes 

"""
What are Present in Attributes?
Attributes in Python can store various types of data. They can hold:

Primitive Data Types (e.g., integers, floats, strings, etc.)
Collections (e.g., lists, dictionaries, tuples, sets)
Objects of Other Classes
Functions (Methods)
Dynamic Values (Created at runtime)
"""

# Example for Each Type

class Example:
    # Class Attribute
    pi = 3.14  # Primitive Data Type (float)

    def __init__(self, name):
        # Instance Attributes
        self.name = name            # String (Primitive)
        self.scores = [85, 90, 88]  # List (Collection)
        self.details = {            # Dictionary (Collection)
            "age": 20,
            "city": "Hyderabad"
        }

    # Method as an Attribute
    def greet(self):
        return f"Hello, {self.name}!"

# Creating an instance
obj = Example("Ravi")

# Accessing Different Types of Attributes
print(obj.name)       # Output: Ravi (String)
print(obj.scores)     # Output: [85, 90, 88] (List)
print(obj.details)    # Output: {'age': 20, 'city': 'Hyderabad'} (Dictionary)
print(obj.greet())    # Output: Hello, Ravi! (Method Output)
print(Example.pi)     # Output: 3.14 (Class Attribute)


"""
Summary
✔️ Attributes can hold:

Numbers (e.g., int, float)
Strings
Lists, Dictionaries, Tuples, Sets
Other class objects
Functions (when accessed through instances)
Attributes are flexible and can store various data types, making them highly versatile in Python."""

#                                                 # Different types 
"""
Types of Attributes in Python
Python attributes are mainly categorized into three types:

1. Instance Attributes
Defined inside the __init__() method.
Unique to each object (instance).
Accessed using object.attribute.
"""
# Example

class Car:
    def __init__(self, brand, color):
        self.brand = brand    # Instance attribute
        self.color = color    # Instance attribute

# Creating instances
car1 = Car("Toyota", "Red")
car2 = Car("Honda", "Blue")

print(car1.brand)   # Output: Toyota
print(car2.color)   # Output: Blue


"""
2. Class Attributes
Defined outside the __init__() method.
Shared across all instances.
Accessed using ClassName.attribute or object.attribute."""

# Example

class Student:
    school = "XYZ School"  # Class attribute

    def __init__(self, name):
        self.name = name  # Instance attribute

# Creating instances
student1 = Student("Ravi")
student2 = Student("Kiran")

print(student1.school)  # Output: XYZ School
print(student2.school)  # Output: XYZ School

# Modifying class attribute
Student.school = "ABC School"
print(student1.school)  # Output: ABC School
print(student2.school)  # Output: ABC School

"""
3. Static Attributes
Similar to class attributes but defined using the @staticmethod decorator.
They don't depend on class or instance data.
Accessed directly via ClassName.method()."""

# Example

class Math:
    @staticmethod
    def add(x, y):
        return x + y

print(Math.add(5, 3))  # Output: 8

"""
Key Differences
Attribute Type   Defined In     	 Shared/Unique	                Access Method
Instance	   Inside __init__()	Unique to instance	           object.attribute
Class	       Outside __init__()	Shared across instances	       ClassName.attribute
Static      	@staticmethod	    Independent of class/instance	ClassName.method()
"""
#                                                 #   data members/Fields/state these
"""
Data Members / Fields / State in Python
In Python, the terms data members, fields, and state generally refer to attributes that hold data within a class.
 While these terms are often used interchangeably, there are slight distinctions in their context:

1. Data Members
Variables that store data within a class.
Can be either instance variables or class variables.

"""

# Example 

class Car:
    wheels = 4    # Class data member (shared across instances)

    def __init__(self, brand, color):
        self.brand = brand  # Instance data member (unique to each object)
        self.color = color  # Instance data member

# Creating instances
car1 = Car("Toyota", "Red")
car2 = Car("Honda", "Blue")

print(car1.brand)  # Output: Toyota
print(car2.wheels) # Output: 4


"""
2. Fields
Another term for data members. Often used in database-related contexts or when discussing class design.
Fields can be public, private, or protected.
"""
# Example 

class Employee:
    company = "TechCorp"  # Public field (accessible from anywhere)
    
    def __init__(self, name, salary):
        self.name = name      # Public field
        self._role = "Staff"  # Protected field (conventionally private)
        self.__salary = salary  # Private field (not directly accessible)

# Accessing fields
emp = Employee("Ravi", 50000)
print(emp.name)         # Output: Ravi
print(emp._role)        # Output: Staff
# print(emp.__salary)   # Error (private field)
print(emp._Employee__salary)  # Output: 50000 (Name Mangling trick)

"""
3. State
Refers to the current values of an object's data members.
The state can change as attributes are modified.
"""
# Example


class Lamp:
    def __init__(self):
        self.is_on = False  # Initial state

    def switch_on(self):
        self.is_on = True  # State changed to ON

    def switch_off(self):
        self.is_on = False  # State changed to OFF

# Creating an object
lamp = Lamp()
print(lamp.is_on)  # Output: False (Initial state)

lamp.switch_on()
print(lamp.is_on)  # Output: True (State changed)

"""
Summary
Term                   Meaning                              	Example
Data Members	Variables that store data in a class	      self.name, wheels
Fields	      Another term for data members (often in OOP)	  self.__salary, company
State	     The current values of an object's data members	  self.is_on = True
"""