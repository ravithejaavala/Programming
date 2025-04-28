# 15-03-25
'''

map()
filter()
reduce()

filter():
--------
the filter() method filters the given sequence with the help of a function that tests
each element in the sequence to be true or not.

syntax:
-----
filter(function_name, sequence)

print()
len()
list()
tuple()

'''


def wish(n):

    return n % 2 == 0
n = [1,2,3,4,5] # global variable
res = filter(wish, n)

print(type(res))

print(list(res))



'''
map() function:
-------------
The map() function is used to apply a given function to every item of an iterbale such as
list, tuple and returns a map object( which is an iterator)


sytax:
-----
map(function_name, iterable)

'''

n = [1,2,3,4]

def squ(val):
    return val**2
res = map(squ, n)

print(list(res))


'''
reduce() function:
-----------------
The reduce() function is used to apply a particular function passed in its argument to all
of the list elements mentioned in the sequence passed along...

this function is defined in "functools" module

syntax:
----

functools.reduce(function_name, iterable)


'''

from functools import reduce

def add(x,y):
    return x+y
n = [1,2,3,4]
res = reduce(add, n)
print(res)


# lambda() function using reduce()
n = [1,2,3,4]
res = reduce(lambda x,y : x+y, n)
print(res)


'''
modules
packages
libararies

OOPS


'''