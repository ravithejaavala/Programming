# 25-03-25
'''

Private members:
--------------
Private members are identified with a double underscoer __ and can't be accessed directly
from outside of the class.

'''

class Emp:

    def _init_(self):
        self.__name = 'hyma' # private members
        self.__gender = 'female'

    def get(self):
        print(self._name, self._gender)

hyma = Emp()
hyma.get()
# print(hyma.__name)


'''
getattr() : to retrieve
hasattr() : it checks if an object has a specific attribute
setattr() : if an object not available it will retur False
delattr() : to delete the attr
'''


class Person:

    def _init_(self, name, age):
        self.name = name
        self.age = age

person = Person('sai',28)

print(getattr(person, 'name'))

print(hasattr(person, 'sal'))

setattr(person, 'sal',25674)

print(getattr(person,'sal'))

delattr(person, 'sal')

# print(getattr(person,'sal'))


name = 'sarath'
last = ' k'

print(name + last)

class Str: # builtin str class

    def _init_(self):
        pass

    def _add_(self, other):
        pass


a = 4
b = 2

print(a*b)


class Int:

    def _init_(self):
        pass

    def _mul_(self, other):
        pass

# *** In python everything an object