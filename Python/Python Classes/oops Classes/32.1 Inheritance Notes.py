"""
Inheritance is a fundamental concept in object-oriented programming (OOP) that allows one class (child)
to inherit the attributes and methods of another class (parent).

Types of Inheritance in Python
Python supports different types of inheritance:

1.Single Inheritance - One class inherits from another.

2.Multiple Inheritance - A class inherits from multiple classes.

3.Multilevel Inheritance - A class inherits from another class, which itself is derived from another class.

4.Hierarchical Inheritance - Multiple child classes inherit from a single parent class.

5.Hybrid Inheritance - A combination of multiple types of inheritance.

"""

# 1. Single Inheritance ----------------------------------

class Parent:
    def greet(self):
        print("Hello from Parent!")

class Child(Parent):
    def show(self):
        print("Hello from Child!")

# Creating object
c = Child()
c.greet()  # Inherited method from Parent
c.show()   # Child's own method

# 2. Multiple Inheritance ----------------------------------

class Father:
    def father_method(self):
        print("This is Father class")

class Mother:
    def mother_method(self):
        print("This is Mother class")

class Child(Father, Mother):
    def child_method(self):
        print("This is Child class")

c = Child()
c.father_method()
c.mother_method()
c.child_method()

# 3. Multilevel Inheritance ----------------------------------

class Grandparent:
    def grandparent_method(self):
        print("This is Grandparent class")

class Parent(Grandparent):
    def parent_method(self):
        print("This is Parent class")

class Child(Parent):
    def child_method(self):
        print("This is Child class")

c = Child()
c.grandparent_method()
c.parent_method()
c.child_method()

# 4. Hierarchical Inheritance ----------------------------------

class Parent:
    def parent_method(self):
        print("This is Parent class")

class Child1(Parent):
    def child1_method(self):
        print("This is Child1 class")

class Child2(Parent):
    def child2_method(self):
        print("This is Child2 class")

c1 = Child1()
c2 = Child2()
c1.parent_method()
c2.parent_method()

# 5. Hybrid Inheritance (Combination of multiple types)----------

class A:
    def method_A(self):
        print("Method A")

class B(A):
    def method_B(self):
        print("Method B")

class C(A):
    def method_C(self):
        print("Method C")

class D(B, C):
    def method_D(self):
        print("Method D")

d = D()
d.method_A()
d.method_B()
d.method_C()
d.method_D()

# Method Overriding in Inheritance -----------------------------

# If the child class has a method with the same name as the parent, it overrides the parent’s method.

class Parent:
    def show(self):
        print("Parent class method")

class Child(Parent):
    def show(self):
        print("Child class method")

c = Child()
c.show()  # Calls the overridden method in Child class
