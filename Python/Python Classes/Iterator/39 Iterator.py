# 09-04-25
'''
Iterator:
------------
An iterator in python is an object that holds a sequence of values and provide sequential
traversal through a collection of items such as lists, tuples and dictionaries...
The python iterators object is initialized using the iter() method... It uses the next()
method for iteration...


_iter_ () : this method initializes and returns the iterator object itself

_next_ () : this method retrieves the next available item, throwing a StopIteration
exception when no more items are available..

-------------OR--------------------------

What are iterators in python:
-------------------------------
Iterator in python is simply an object that can be iterated upon. An object will return
data, *one element at a time*

Iterators are everywhere in python, They are elegantly implemented with in the list,
tuple, generators, comprehension.... but the iterators are hidden in plain sight..

Python iterator object must implement two special methods , _iter() and __next_()
methods, collectively called iterator protocol....

We use the next() method to manually iterate through all items of an iterator and if there
is no element to iterate then it will raises a StopIteration exception...


Difference between iterator and iterable:
---------------------------------
Iterables are objects that can return an iterator...
These includes buil in data strcutres like lists, tuples, dictionaries and sets...
Essentially, an iterable is anything you can loop using over the for loop...
An iterable implements the _iter_() method, which is excepted to return an iterator
object....


'''

name = 'sarath'
it = iter(name)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# print(next(it))


li = [1,2,3,4]
for i in li:
    print(i)
    if i == 3:
        break


# StopIterator Execption

li  = [1,2,3,4,5]
iter = iter(li)

while True:
    try:
        print(next(iter))
    except StopIteration:
        print('end of the execution')
        break


# iterators in python


class Square:
    def _init_(self, max = 0):
        self.max = max
    def _iter_(self):
        self.n = 0
        return self
    def _next_(self):
        if self.n <= self.max:
            res = 2 ** self.n
            self.n += 1
            return res
        else:
            raise StopIteration

sq = Square(4)
# myiter = iter(sq)
# next(myiter)
# next(myiter)
# next(myiter)
# next(myiter)

print('---iterator----')
for i in sq:
    print(i)


class Even:
    def _iter_(self):
        self.p = 2
        return self
    def _next_(self):
        x = self.p
        self.p += 2
        return x
even = Even()
ite = iter(even)
print(next(ite))