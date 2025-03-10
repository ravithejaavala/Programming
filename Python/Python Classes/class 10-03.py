'''
Frozenset data type:
---------------------
Frozenset is an immutable data type.

The only difference set vs frozenset is - set becomes mutable and frozenset becomes immutable...

Frozenset is created by using the built in function : frozenset()

Frozenset also doesn't allows duplicates..

There is no indexing and slicing operations in frozenset()

not able to update or add the element to the existing frozenset()

syntax:
-----
frozenset(iterable_object)


'''
fro_set = frozenset()
print(type(fro_set))


li = [1,2,3,4]

res = frozenset(li)
print(type(res))
print(res)
#
# res.add('sarath')
#
# print(res)


'''
Dictionary data type:
-------------------

collections module: ***************

1. OrderedDict
2. DefaultDict
3. Counter
4. namedtuple

OrderedDict in python:
--------------------
An OrderedDict is a dictionary sub class that remebers the order in which keys were first
inserted. The only difference between dict() and OrderedDict() handling key order..

- OrderedDict maintains the sequence in which keys are added, ensuring that the order is
preserved during the iteration...



'''

dic = {'name':'ravi','age':28,'gender':'male'}
print(dic)


set = {1,2,'ravi','sarath',3}
print(set)


dic = {}
dic['emp_name'] = 'sarath'
dic['age'] = 30

print(dic)


from collections import OrderedDict

od = OrderedDict()
od['one'] = 1
od['two'] = 2
print(od)


'''
Defaultdict:
-----------
The Defaultdict is a container like dictionaries present in the collections module..

It is a sub class of the dictionary class that returns a dictionary like an object..
So, the main difference from dict vs Defaultdict is , it provides a default value for the key
that does not exist and it never raises a KeyError..

'''

details = {'name': 'ravi', 'age': 28, 'gender': 'male'}

# print(details['sal'])
# print(details.get('sal'))



from collections import  defaultdict

dd = defaultdict(lambda : 'make sure that key does not exists in the defaultdict')
dd['name'] = 'sai'
dd['age'] = 28
print(dd)

print(dd['gender'])