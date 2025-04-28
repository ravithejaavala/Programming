# 24-03-25
'''
static variables and static methods


'''


# static variable and static method

class Product:

    product_count = 0 # static variable

    def _init_(self, name, price):
        self.name = name
        self.price = price
        Product.product_count += 1

    @staticmethod
    def get_product_count():
        return Product.product_count

prod1 = Product('iphone',324567)
prod2 = Product('andriod',235634)

res = Product.get_product_count()
print(res)


'''
IV IM
CV CM
SV SM


CV IM -- have covered?
IV CM : The instance variables are not able to access inside the class method..**

'''


class Emp:

    def _init_(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def get_details(cls):
        print(cls.name, cls.age)

sarath = Emp('sarath',30)
# sarath.get_details()


'''

Encapsulation:
------------


In python, the encapsulation refers to the building of data(attributes) and methods(functions)
that operate on the data into a single unit, typically a class...
It also restricts direct access to some components, which will helps protect the integiry
of the data and ensures proper usage...

How encapsulation works?

Data hiding:
-----
The variables (attributes) are kept private or proctected, meaning they are not accessible
directly from outside of the class. Instead, they can only be accessed or modified through
the methods...



There are 3 ways:

1. public members
2. protected members
3. private members

getattr()
setattr()
hasattr()
delattr()

'''

#1. public members : we can access from anywhere, both inside and outside of the class

class SoftwareEng:

    def _init_(self):
        self.name = 'hyma' # public attribute
        self.age = 28
    def get_emp_details(self):
        print(self.name, self.age) # public method

hyma = SoftwareEng()
hyma.get_emp_details() # accessing the instance
print(hyma.name) # accessing the public attribute out of the class


'''
2. protected members:
-------------------
Protected members are identified with a single underscore(_) . They are meant to be
accessed only within the class or its sub classes

How to identify the protected members?

The attribute with a sigle underscore, which by convention suggests that is should be treated
as a protected member. So it's not enforced by python but it indicates that it should
not be accessed outside of this class and it's sub class


'''

class Stundent:

    def _init_(self):
        self._name = 'ravi' # protected attribute
        self._age = 26
        self._gender = 'male'

    def get(self):
        print(self._name, self._age, self._gender) # protected methods

ravi = Stundent()
ravi.get()
print(ravi._gender)