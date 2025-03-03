'''

Memory allocation:
----------------------


stack memory
heap memory



name='dinesh' # value/object

name - variable (references)


stack memory:
--------


the method calls and the references are stored in the stack memory ...

the allocation happens on contiguous blocks of memory. We call it stack memory because
the allocation happens in the function call stack...

heap memory:
--------------

The values or objects stored in the heap memory..

THe memory is allocated during the execution of instructions written by the programmer.
Note that the heap has nothing to do with the heap data structure...





'''
name = 'dinesh'
print(name)



'''

Variables in python:
-------------------

Variables are used to store the data that can be referenced and manipulated during
the program execution. A variable is essentially a name that is assigned to a value/object.

---------------or-------------------

A variable is a name which is used to refer the memory location of a value. Variable
is also know as identifier and which is used to hold the value.
In python , we don't need to specify the type of variavble(int, str) because python
is a dynamically typed programing language..


pep8 in python : **********************


Rules for naming the variables:
-----------------------

1. Varible names can only contain letters, digits and underscores
2. Variable name cannot start with a digit
3. Variable names are case sensitive
4. Avoid using the keywords as a variable names.

'''

name = 'sarath'

n = 88


nam = 'HYMA'

NAM = 'sarath'

print(id(nam))

print(id(NAM))

first_2_last = 'python'

# 1name = 'k' - not applicable

'''
for if else
and or not
class yield

'''
# for = 'python'
# print(for)

# valid example for variable name


name = 'sarath'
_age = 30 # procted variable
first_last = 'programing'


# invalid variable names

# 1gender = 'male'
# and = 'and' - and is a keyword in python, so we are not supposed to be use a variable name
# first-last = 'sarath'



# assinging values to the variable


x = 33
print(x)

# multiple assignments

a = b = c = 22
print(c)

print(id(a))
print(id(b))
print(id(c))


# multiple variables with multiple values

name,age, gender = 'sarath',30,'male'
print(name)
print(age)
print(gender)

'''
Type casting in python:
----------------------
Type casting refers to the process of converting the value of one data type into
the another data type. Python provides several built in functions to facilitate the
type cating , for example int(), str(), list().....

int() - converts comptaible values into interger
str - converts into string


'''


s = '10' # single represnts string

print(type(s))

con_integer = int(s) # type casting by using the int()
print(con_integer)

print(type(con_integer))

# convert to float

num = 23
conver_floa = float(num) # type casting by using the float()

print(conver_floa)

print(type(conver_floa))

'''
constants: **************
---------
A constant is a type of variable whose value cannot be changed all the time..


scope of variables:
------------------
local variables
global variables

'''

NAME = 'ravi' # constant


'''
python : https://www.python.org/downloads/

pycharm : https://www.jetbrains.com/pycharm/download/?section=windows (community version)


'''