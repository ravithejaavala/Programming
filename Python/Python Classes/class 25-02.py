'''

slicing operations:
----------------------


slicing operations allows us to extract the part of the string. We can specify
the start index, end index and step also.
the general format of slicing is:

*string[start:end:step]*

name = 'sarath'

print(name[0])

print(name[0:3]) - 0 is starting index
                 - 3 is an ending index (end index should be calculated as 0 : n-1)
'''

name = 'sarath'

print(name[0]) # indexing

print(name[0:3])

print(name[0:7:3])

'''
Data types:
------------

Data types are the classification or categorization of the data items. It represents
the kind of value that tells what operations can be perfomed on a particular data.
Since everything is an object in python. So the python data types are classes
and variables are the instance(object) of the classes.

Types of data types:
------------------

Numeric - int, float, complex **
 
Sequence type - string, list, tuple ******

Mapping type - dict *************

Set type - set, frozenset ****

Binary types - bytes, bytearray

Boolean - bool



mutable data type and immutable data type

name = 'hyma'
name[1] = 'e'

TypeError: 'str' object does not support item assignment

immutable data types are the best:

Numeric data types:
------------------

The numeric data type in python represents the data that has a numeric value. A
numeric value can be an integer, a floating number or even the complex number.
These are defined as python int, python float, python complex classes in python...

All three data types (int, float, complex) are the immutable data types..

Integer:
-------
This value is represented by the int class. It contains both positive and negative
numbers. There is no limit to how long an interger value can be...

Float:
----
This value is represented by the float class. It is specified by the decimal
point...


complex number:
-----------------
A complex number is represented by the complex class. It is specified as a
real part + imaginary part.

for example : 2+3j


'''
nam = 'sarath'
li = [1,2,3]
name = 'hyma'
# name[1] = 'e'
print(name)

li.append('sarath')
print(li)

print(nam)


n = 99
print(n)
print(id(n))

n = 12
print(n)
print(id(n))

print(type(n))


m = 33.43
print(type(m))


res = 2+3j

print(type(res))

print(res)