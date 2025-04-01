# 01-04-25

'''

Types of inheritance:
---------------------
single inheritance
multi level inheritance
multiple inheritance
hierarchical inheritance


multi level inheritance:
------------------------
In multilevel inheritance, features of the base class and the derived class are futher
inherited into the new derived class. This is similar to a relationship representing
a child and grand father...

A  - Base class/parent class

B  - Intermediatory class

C  - Child class


'''

class Grandfather:

    def _init_(self, grandfathername):
        self.grandfathername = grandfathername

class Father(Grandfather):

    def _init_(self, grandfathername, fathername):
        self.father = fathername
        super()._init_(grandfathername)

class Son(Father):

    def _init_(self, grandfathername, fathername, sonname):
        self.sonname = sonname
        super()._init_(grandfathername, fathername)

    def details(self):
        print(self.grandfathername, self.father,self.sonname)

bharath = Son('siva','ramana','bharath')
bharath.details()



'''
Multiple inheritance:
------------------
When a class can be derived from more than one base class this type of inehritance is
called multiple inheritance. In the multiple inheritances, all the features of the base
classe are inherited into the derived class...

    class A             class B   -- A & B are parent class/base class
        
            
            class C(A,B) -- child class


MRO (Method Resolution Order):
--------------------
The MRO defines the sequence in which classes are searched for methods or attributes..

How it works?

1. The MRO follows a depth-first, left to right fashion(approach)
2. It initially starts by searching the current class
3. If any method/attribute is not found, then it searched into the parent classes, strting from
    the left-most parent class in the inheritance list
4. This process continues until the method/attribute is found or the searche reaches the
    object class...
5. The interperter won't read the class more than 1 time. It read the classes only once..

'''


class SoftwareEmp: # parent class

    def _init_(self, id, age):
        self.id = id
        self.age = age

class GovtEmp: # parent class

    def _init_(self, name, sal):
        self.name = name
        self.sal  = sal

class Emp(SoftwareEmp, GovtEmp): # child class

    def _init_(self, id, age, name, sal):
        GovtEmp._init_(self, name, sal)
        super()._init_(id, age)

    def get_emp_details(self):
        print(self.id, self.age ,self.name, self.sal)

ravi = Emp(1, 27, 'ravi',32456789)
ravi.get_emp_details()


'''
Herarchical inheritance:
---------------------
When more than one derived class or child class are created from a single base class
this type of inheritance is called hierarchical inheritance..

                    class A # parent class
        
class B         class C         Class D # child class



'''


class Parent:

    def fun1(self):
        print('this function/method in the parent class')

class Child1(Parent):

    def fun2(self):
        print('this method in the child 1 class')

class Child2(Parent):

    def fun3(self):
        print('this method in the child 2 class')

obj1 = Child1()
obj1.fun2()
obj1.fun1()


obj2 = Child2()
obj2.fun3()
obj1.fun1()


# since everything is an object ...


a = 9
b = 8
print(a+b)


class Object:

    class Int(object):
        pass
        class Str:
            pass
            class List:
                pass