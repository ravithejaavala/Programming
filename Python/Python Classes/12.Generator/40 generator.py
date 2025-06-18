# 12-04-25

'''


Generators:
-----------
There are 2 types of generators:

1. generator function
2. generator object


1. generator function:
--------------------------

A generator function is  a special type of function that returns an iterator object.
Insted of using return to send back a single value, generator functions use *yield*
keyword to produce a series of results over time...
This allows the function to generate values and pauses its execution after each yield,
maintaining it's state between iterations...


syntax:
----

def func(parameters):
    #code
    yield expression
func(arguments)


'''

def wish(max):
    count = 0
    while count <= max:
        yield count
        count += 1
res = wish(5)
print('-------------')
it = iter(res)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# print(next(it))

print('--using for loop-----')
for i in res:
    print(i)



'''
yield vs return statements:


yield is used in generator functions to provide a sequence of values over time. When
yield is executed, it pauses the function, returns the current value and retains the
state of the function. This allows the function to continue from the same point when
called again, making it ideal for generating the large or complex sequences efficiently..


Return:
return is used to exit a function and return a final value. Once return is executed,
the function is terminate immediately, and no state is retained. This is suitable for cases
where a single result is needed from a function...




generator expression or generator object:
------------------------------
Generate expressions are a concise a qay to create the generators...

list comprehension
dict comprehension
set comprehension...

list comprehension:
----------------
list comprehension offers a shorter sytanx when you want to create a new list based
on the values of an existing list...


syntax:
----
newlist = [i for i in input if condition]

'''

def dis():

    print('hello all!!')

res = dis()
print(res)



# the normal list


lis = [1,2,3,4,5]
newlist = []
for i in lis:
    res = i ** 2
    newlist.append(res)
print(newlist)


# list comprehension

lis_com = [i**2 for i in lis if i % 2 == 0]
print(lis_com)