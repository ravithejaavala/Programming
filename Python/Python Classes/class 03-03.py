'''

list methods:
----

15 - methods


'''

li = list() # []

print(type(li))

# append() : this method add the elements at the end of the list. And make sure
# it will add only one element at a time

lis = [1,2,3,4]
lis.append('dinesh')
print(lis)

# clear() : this method removes all the elements inside the list

li = [1, 2, 3, 4, 'dinesh']
li.clear()
print(li)

# count() : this method returns the number of times an element appears in the list

li = [1, 2, 3, 4, 'dinesh']
res = li.count(2) # 2 is an element
print(res)

# extend() : this method adds all the elements of the specified iterable to
# the end of the list

li = [1,2,3]
li1 = [4,5,6]
li1.extend(li)
print(li1)

# index() : this method returns the index of the specified element at the list
# if element not found then it will raise an exception(ValueError)

li = [1,2,3]
res = li.index(3) # 3 is an element
print(res) # 2 - index


# insert() : this method inserts an element to the list at the specified index

li = [1,2,3]
print('before inserting',li)
li.insert(0,'hyma sree')
print('after inserting',li)
li.insert(4,'sarath')

print('--',li)


# pop() : This method removes the item at the specified index.. The method also
# returns the removed item..

new_li = ['hyma sree', 1, 2, 3, 'sarath']
res = new_li.pop(4) # 4 is an index
print(res)
print(new_li)

# remove() : This method removes the first matching element from the list

new_li = ['hyma sree', 1, 2, 3, 'sarath',1]
new_li.remove(1)
print(new_li)

# reverse() : this method reverse the elements from the list
new_li = ['hyma sree', 1, 2, 3, 'sarath',1]
new_li.reverse()
print(new_li)

# sort() : this methods sorts the elements in an ascending/descending order

li = [1,123,2,55,-1,0]
li.sort()
print(li)
li.sort(reverse=True)
print(li)


# copy()