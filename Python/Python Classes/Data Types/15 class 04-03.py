'''
copy() method in list:

There are two types of copies which we have:

We need to import copy module first

1. shallow copy :
------------
a. shallow copy stores the references of objects to the original memory address.
b. Shallow copy reflects changes made to the new/copied object in the original object
c. Shallow copy stores the copy of the original object and points the references to the objects.
d. A shallow copy is faster

2. deep copy:
------------
a. Deep copy stores copies of the object value's.
b. Deep copy doesn't reflect changes made to the copied object in the original object
c. Deep copy stores the copy of the original object and recursively copues the objects as well
d. Deep copy is bit slower as compared to shallow copy

'''


import copy

nes_li = [1,2,3,[4,5,6]]
copied = copy.copy(nes_li)
print(copied[0])

copied[3][0] = 'sai kumar'

print(nes_li)

print('---', id(nes_li))
print(id(copied))
# deep copy

nes_li = [1,2,3,[4,5,6]]
new_copy = copy.deepcopy(nes_li)
print(new_copy)

new_copy[0] = 'sarath'
print(new_copy) #
print(nes_li) #

print(id(new_copy))
print(id(nes_li))

# type conversion from list to tuple

li = [1,2,3]
tup = tuple(li)
print(type(tup))
print(tup)

'''
Tuple data type:
-----------------
Tuple is an immutable data type, once we can create the data we can't able to change or we can't
able to modify it...

Notes:******
-----
1. Tuple is represented by the paranthesis ()
2. Elements are separated by the comma (,)
3. Tuple data type allows the homogenous and heterogenous data types
4. Tuple also allows the duplicates
5. Nested tuple also works

CRUD operations

'''

# create operation

tup = ('sarath', 'hyma','sai','ravi',1,2.2,1)

print(tup)

# retrieve operation

tup = ('sarath', 'hyma','sai','ravi',1,2.2,1)
print(tup[0]) # indexing mechanism

for i in tup:
    print(i)
    if i == 'sai':
        break

# update operation

tup1 = (1,2,3,)
# tup1[0] = 33
tup2 = (4,5,6)
res = tup1+tup2
print(res)


# delete operation

tup1 = (1,2,3,)
del tup1
# print(tup1)

# nested tuple
tup1 = (1,2,3,(4,5,6,(7,8,9)))

print(tup1[3][3])

# list inside the tuple

tup = (1,2,3,[7,8,9,(10,11)])
print(tup[3])
tup[3][2] = 'sarath'
print(tup)

# type conversion from tuple to list
tu = (1,2,3,(4,5,6,(7,8,9)))
lis = list(tu)
print(lis)

# tuple methods in python

# count() : this method returns the number of times the specified element appears in the tuple

tu = (1,2,3,(4,5,6,(7,8,9)),1)
res = tu.count(1)
print(res)


# index() : This method returns the index of the specified element in the tuple, if element not ffound then it will throw an error

tu = (1,2,3,(4,5,6,(7,8,9)),1)
ind = tu.index(2) # 2 is an element
print(ind)


# As compared to the list vs tuple which is better???