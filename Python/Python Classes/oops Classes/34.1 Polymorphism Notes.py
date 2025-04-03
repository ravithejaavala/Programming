# Polymorphism in Python
#------------------------------
"""
--->Polymorphism means "many forms." It allows the same function or method to have different behaviors depending on the object that is calling it.

 Types of Polymorphism in Python
1. Method Overriding (Already covered) - A child class provides a new implementation of a method from its parent class.
2. Method Overloading - Python does not support method overloading like Java or C++, but we can achieve similar behavior using default arguments or *args.
3. Operator Overloading - We can define how operators (+, -, *, etc.) work for custom objects.

"""
# 1. Polymorphism with Method Overriding (Same method, different behavior)

class Animal:
    def make_sound(self):
        print("Animals make sounds")

class Dog(Animal):
    def make_sound(self):  # Overriding method
        print("Dog barks")

class Cat(Animal):
    def make_sound(self):  # Overriding method
        print("Cat meows")

# Polymorphism in action
for animal in [Dog(), Cat()]:  # Both have `make_sound()` but behave differently
    animal.make_sound()

# output
"""
Dog barks
Cat meows
"""

#✅ The same method make_sound() behaves differently for Dog and Cat.

#-------------------------------------------------------------------------------------------

# 2. Polymorphism with Method Overloading (Same method, different parameters)

"""Python does not support true method overloading, but we can achieve it using default values or *args."""

class MathOperations:
    def add(self, a, b, c=0):  # Default value allows different parameter counts
        return a + b + c

math = MathOperations()
print(math.add(10, 20))       # Calls add with 2 parameters
print(math.add(10, 20, 30))   # Calls add with 3 parameters

# output
"""
30
60
"""

# ✅ The add() method works with both two and three parameters, simulating method overloading.

#-------------------------------------------------------------------------------------------

# 3. Operator Overloading (Customizing Operators for Objects)
"""
Python allows us to define how operators work for custom objects by overriding magic methods (dunder methods).

-> Example: Overloading the + Operator for a Custom Class
"""
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __add__(self, other):  # Overloading `+`
        return self.pages + other.pages

book1 = Book("Python Basics", 200)
book2 = Book("Advanced Python", 300)

print("Total pages:", book1 + book2)  # Calls book1.__add__(book2)

# output
"""
Total pages: 500
"""

# ✅ The + operator is customized to add pages of books instead of numbers.

#-------------------------------------------------------------------------------------------

# 🔹 Summary of Polymorphism Concepts

"""
      Type	                       Definition	                            Example
1.Method Overriding	   Child class redefines a parent method	    Dog.make_sound() and Cat.make_sound()
2.Method Overloading	   Same method name, different parameters  (simulated using *args or default values)	
                                                                    add(a, b) and add(a, b, c)
3.Operator Overloading   Defining custom behavior for operators	    Overloading + to add book pages

"""