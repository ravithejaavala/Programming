'''

data types:
-----------


name = 'hyma' # value/object

m = 88
n = 77

print(m+n)

li = [1,2,3]

# In python, everything is an object...

In python, every variable was holds an instance of an object...
There are two types of objects in python i.e,,,
'mutable' and 'immutable' objects. **************

C R U D operations:

C - Create

R - Retrieve

U - Update

D - Delete


mutable object:
------------

Mutable object is nothing but once we can create the data , we can able to change
or we can able to modify it.

li = [1,2,3] # object --> mutable object


data types which comes under mutable data type:

1. list
2. dict
3. set

Note: after creation of the object, even if you can made the changes the address of
the object should be the same...

immutable data types or objects:
-------------------------------

If the object is an immutable data type, once we can create the data we can not able
to change or we can't able to modify it.
If you still try to modify it will throw as an error.

name = 'sai'
name[1] = 'a'
print(name)

For the above it will throw as an error.

TypeError : str object does not support to the item assignment..

data types which comes under immutable data types:
----

string
int
float
complex
tuple
frozenset



indexing and slicing operations:

In python, indexing and slicing operations are techniques used to access the
specific characters or set of characters or parts of a string.
*Indexing* means referring to an element of an iterable by its position...
where as *slicing* is a feature that enables accessing parts of the sequence..

name = 'hyma sree'

indexing operations:
------------------
String indexing allows us to access the individual characters or elements in a string.
indexing operations to retrieve the data , we can use the list opertions *[]*.

The indexing mechanism starts with 0 from left to right fashion....

indexing mechanism starts with -1 from right to left fashion...

slicing operations:
----------------------


slicing operations allows us to extract the part of the string. We can specify
the start index, end index and step also.
the general format of slicing is:

*string[start:end:step]*

'''

li = [1,2,3] # object --> mutable object
print(id(li))

print(li)

li.append('sarath')

print(li)
print(id(li))


name = 'sai'
# name[1] = 'a'
print(name)


name = 'hyma sree'

print(name[0])

print(name[-1])