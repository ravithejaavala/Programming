# 09-03-25
'''

dict methods:
------------

pop()

popitem()
'''

# pop() : this method removes and returns an element from a dict having the given key..

dic = {'name':'hyma','age':28,'gender':'female'}

removed_ele = dic.pop('gender')
print(removed_ele)


#popitem() : this method removes and returns item(key, value) pair from the dict in the LIFO order
dic = {'name':'hyma','age':28,'gender':'female'}
res = dic.popitem()
print(res)
res = dic.popitem()
print(res)
res = dic.popitem()
print(res)
# res = dic.popitem()
# print(res)


'''
Set data type:
--------------


The whole set is a mutable data type, which means once we can create the data, we can able to
change or modify it.. But inside of the elements are immutable

***Set follows un-ordered data type

Set is represetned by the curly braces {}

Priority wise if it is an empty curly braces then it goes to *dict*

Set doesn't allows the duplicate elements. If try to insert the same item again, it overwrites previous one

In set data type there is no indexing and slicing mechanism..

An unordered collection. When we access all items, they are accessed without any specific order
and we can't access items using the indexing ...

Internally use *hashing* that makes set efficient for search, insert and delete opertions. It
gives a major advantage over a list for problems with these opertions



'''

set = {1,2,3,'sai'}

print(type(set))

print(set)


# create opertions

# create_set = set()
# print(create_set)

set = {1,2,3}
print(set)

# retrieve operation

for i in set:
    print(i)

# update operation


set = {1,2,3}

set.add('hyma sree')
print(set)

# delete operation

set_ele = {1, 2, 3, 'hyma sree'}
set_ele.discard(1)
print(set_ele)

'''
fronset() data types

collections module:

dict : un-ordered

default dict
ordered dict
namedtuple
counter






'''


# set methods

# add : this method adds a given element to a set, if element is already present it doesn't add any element

set_ele = {1, 2, 3, 'hyma sree'}
set_ele.add('sarath')
print(set_ele)


# clear() : this method removes all items from the set

set = {1, 2, 3, 'hyma sree', 'sarath'}
set.clear()
print(set)


# copy() : this method returns a copy of the set

set = {1, 2, 3, 'hyma sree', 'sarath'}
new = set.copy()
print(new)

# intersection() : this method returns a new set with the elements that are common to all sets

set1 = {1,2,3,4,5}
set2 = {4,5,6,7}
print(set1.intersection(set2))


# union() : this method returns a new set with distinct elements from all the sets..
set1 = {1,2,3,4,5}
set2 = {4,5,6,7}
print(set1.union(set2))

# update() : this method updates the set adding items from other iterables

set1 = {1,2,3,4,5}
set2 = {'sarath','dinesh'}
set1.update(set2)
print(set1)


# pop() : this method removes an item from a set and returns the removed item

new_set = {1, 2, 3, 4, 5, 'dinesh', 'sarath'}
res = new_set.pop()
print(res)
print(new_set)


# remove() : this method removes the specified element from the set

new_set = {1, 2, 3, 4, 5, 'dinesh', 'sarath'}
new_set.remove(1)
print(new_set)