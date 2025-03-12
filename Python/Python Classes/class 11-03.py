'''

collections:

defaultdict
orderedict
counters
namedtuple


counters:
-------

A counter is a sub class of the dictionary. It is used to keep the count of the elements in an
iterable in the form of unordered dictionary where the *key* is reperesents the element in the
iterable and *value* is represents the count of that element in the iterable
'''

from collections import Counter

li = [1,2,3,1,2,4,5,6,4,5]

res = Counter(li)
print(res)


'''
NamedTuple:
-----

NamedTuple is present inside the collections module. It provides a way to create simple, light
weight data structures similar to a class, but without the overhead of defining a full class.
Like dictionaries, they contain keys that are hased to a particular value..



syntax:
-------

namedtuple(typename, fields)
typename - class name
fileds - attributes

'''

from collections import namedtuple

Employee = namedtuple('Employee',['emp_name','age','sal'])
res = Employee('hyma',28,235678)
print(res)
res = Employee('sarath',30,6789876)
print(res[0])
print(res[1])
print(res[2])
# print(res[3])
print(res.emp_name)



'''
Functions:
----------

Python functions is a block of code or block of statements that return the specific task..
The idea is to put some commonly or repeatedly done task together and make a function so that
instead of writing the same code again and again for different inputs, we can do the function calls
to reuse code contained in it over and over again..


Benefits:
----
Increase the Code Readability
Increase the Code Reusability..


Function Declaration:
--------------
def function_name(parameters):
    # body of the function

function_name(arguments) -- calling the function




'''

a = 1 # we are hard coding the value
b = 2

print(a+b)

def add(a,b):
    res = a+b
    print(res)
add(1,2)
add(2,2)