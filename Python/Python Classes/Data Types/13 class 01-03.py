'''
data types:
--------------
int
string
list
tuple
dict
set



name = 'shridhar' # object/value


mutable data type
immutable data type


list data type:
-------------
list is a mutable data type, which means that once we can create the data. We can
able to change or we can able to modify it.

A list is a built in dynamic sized array(automatically increase and decrease
size based on the elements). We can store all types of items in the list.

-------or------------------
The list is a most versatile data type available in python, which can be written
as a list of comma separated elements.


Key points:
----------

1. List is represented by the square brackets -- []
2. Each elements is separated by the comma (,)
3. List allows homogenous data types and heterogenous data types are also allowed
4. List allows the duplicates as well
5. List allows nested list as well


lis = [1,2,3] -- 1 2 3 are the elements in python

lis = [1,2,3] --- all the elements are same data type then we can call it as a *homogenous data types*
lis = [1,'hyma','sai'] - different type of elements are also allowed and we can
                         call it as a heterogenous data type


lis = [1,2,3,1,2]

# C R U D operations


'''


li = []

print(type(li))

lis = [1,2,3,1,2]
print(lis)

# list CRUD operations

lis = [1,2,3,4,'sarath'] # create

# retrieve operations

lis = [1,2,3,4,'sarath'] # index starts with 0 (left to right) and index starts -1 (right to left)

print(lis[0])
print(lis[-1])

for i in lis:
    print(i)


# update operation

lis = [1,2,3,4,'sarath']

print(id(lis))

lis[0] = 'dinesh'

print(lis)

print(id(lis))

# lis[5] = 'sai'

print(lis)


# delete operation

li = ['dinesh', 2, 3, 4, 'sarath']

del li[-1]

print(li)


# nested list

nes_lis = [1,2,3,[4,5,6]]

print(nes_lis)
print(nes_lis[3][2])

nes_lis[3][2] = 'hyma'

print(nes_lis)

# example nested

nes_lis = [1,2,3,[4,5,6,[7,8,9]]]

print(nes_lis)
print(nes_lis[3][3][0])

nes_lis[3][3][0] = 'sarath'
print(nes_lis)


# list we have around 15 methods