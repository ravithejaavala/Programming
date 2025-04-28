# 05-03-25
'''

Dictionary data type:
-------------------
The whole dictionary is an mutable data type, which means once we can create the data or object we can
able to change or we can able to modify...

1. Dictionary is represented by the curly braces {}
2. Dict is an *unordered set* of key and value pair.

dic = {}

dic = {'key':'value'}

for example of employee details:

dic = {'name':'sarath','age':30,'sal':3465879}

'name' , 'age', 'sal' -- keys

'sarath', 30, 3465879   -- values

keys : immutable data types only allowed  ************
value : mutable/immutable data types are allowed  ************


3. Each key and value is separated by the colon(:)
4. Key and Value we can consider that as a *item* in dictionary
5. Each item is separated by the comma(,)
6. In dict both homogenous and heterogenous data types are allowed
7. In dict there is no indexing and slicing operation
8. Duplicates are also not allowed in dict, still if we are trying to create the duplicate then
    it will consider the latest *key*

'''


# list and tuple : these two data types are followed by the insertion order or it preserves insertion order

li = [1,2,3]

print(li)

tup = (1,2,'sarath','sai')
print(tup)


dic = {'list':[1,2,3]} # hash() in python
print(type(dic))
print(dic)


# create operations

dic = {'name':'sai','age':26,'gender':'male'}
print(dic)


# retrieve operation : We can able to retrieve the data with the help of keys only

dic = {'name':'sai','age':26,'gender':'male'}

print(dic['name']) # we are providing the key and it returns value

# print(dic[26])


for i in dic.items():
    print(i)


# update operation

dic = {'name':'sai','age':26,'gender':'male'}
dic['name'] = 'ravi'
print(dic)

dic = {'name':'sai','age':26,'gender':'male','name':'bhanu'}

print(dic) # output :

# delete operation

dic = {'name':'sai','age':26,'gender':'male'}

del dic['gender']
print(dic)

del dic
# print(dic)


# 15 methods in dict

dic = {'key':None}

print(dic)


# nested dict