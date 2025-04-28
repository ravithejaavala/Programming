# 14-04-25
'''

list comprehension
dict comprehension
set comprehension


list comprehension:
-----------------

List comprehension is a concise way to create lists based on existing iterables like
lists, tuples, string .... It provides a more readable and often more efficient way to
construct lists compreated to using the traditional for loop ...

syntax:

lis = [expression for item in iterable if condition]

Advantages:
---------
Conciseness: List comprehensions can often achieve the same results as a for loop with
the fewer lines of code, maling the code more compact and easier to read...

Readability : Syntax are straight forward, list creation based on transformations. The
list comprehensions can be more expressive and easier to understand...

Performance :  In few scenarios, list comprehensions can be slightly more performant
than equivalent for loops,, especially for simple opertions, because they are often
optimized internally by the pyton....

'''


lis_names = ['sarath','dinesh','sai','bhanu']

res = [i.upper() for i in lis_names]

print(res)


# nested list comprehension

lis = [[1,2,3],[4,5,6],[7,8,9]]

nest_list_com = [j for i in lis for j in i]
print(nest_list_com)


'''
Dicitionary comprehension:
----------------------------

Dictionary comprehension is a concise way to create dictionaries. It's similar to list
comprehension but allows you to define both keys and values for the dictionary..


syntax:
-----

dic_com = {key:value for key, value in iterable if condition}

key differences between list comprehension and dict comprehension:
-----------------------
The main difference is the structure of the output. List comprehension creates a list
with single elements based on the expression, while dictionary comprehension creates
a dictionary with key-value pairs..

'''


# dict comprehension


dic_com = {'sarath':30,'hyma':27,'dinesh':28}

resp = {name:age for name, age in dic_com.items() if age >= 28}
print(resp)

# 2 lists combined to dict

k = ['a','b','c']
v = [10,100,1000]
combine_dic = {k[i]:v[i] for i in range(len(k))}
print(combine_dic)

'''
set comprehension:
----------------------
Set comprehension is a concise way to create set based on existing iterables. It follows
a syntax very similar to list comprehension, but instead of creating a list, it creates
a set...

syntax:
----
new_set = {expression for item in iterable if condition}

'''


set_in = {}

print(type(set_in))

nums = [1,2,3,4,5,6,7,8,9,10]
result = {i % 3 for i in  nums}
print(result)


# example - 2

lis = [1,2,3,4]
squ_ele = {i**2 for i in lis}
print(squ_ele)