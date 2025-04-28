# 06-03-25
'''

nested dictionary:
---------------
Inside dictionary we need to define one more dictinary then we can consider that as a nested dict..


'''

nest_dic = {'name':'sarath','age':30,'nested_dict': {'gender':'male','sal':4654567}}

print(nest_dic)

nest_dic['name'] = 'sai kumar'

print(nest_dic)
nest_dic['nested_dict']['sal']= 123345

print(nest_dic)


'''
dict methods:
------------

# clear() : this method removes all the items in the dict
'''

dic = {'name': 'sai kumar', 'age': 30, 'nested_dict': {'gender': 'male', 'sal': 123345}}

dic.clear()
print(dic)


# copy() : this method copy the elements returns a shallow copy of the dict

dict = {'name': 'sai kumar', 'age': 30, 'nested_dict': {'gender': 'male', 'sal': 123345}}
print(id(dict))
copied = dict.copy()
print(copied)
print(id(copied))

copied['name'] = 'hyma'

print(copied)

print(dict)

# fromkeys() : this method creates a dict from the given sequence of keys and values

numbers = {1,2,3}

values = 'int'


dictionary = dict.fromkeys(numbers, values)
print(dictionary)



# get() : this method returns the value of the specified key in the dict

dic = {'name1':'sarath','age':30,'address':'blr'}

# print(dic['sal'])

print(dic.get('name', None))


# items() : this method returns list of tuple

dic = {'name1':'sarath','age':30,'address':'blr'}

print(dic.items())

for i in dic.items():
    print(i)


# keys() :

dic = {'name1':'sarath','age':30,'address':'blr'}

print(dic.keys())


for i in dic.keys():
    print(i)

# values()

dic = {'name1':'sarath','age':30,'address':'blr'}

print(dic.values())

# update() :


dic = {'name1':'sarath','age':30,'address':'blr'}

dic1 = {'sal':23455}

dic.update(dic1)

print(dic)