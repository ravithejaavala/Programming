'''


keyword:
--------

Keywords in python are reserved words that have special meanings and specific purpose
we used.


'''


import keyword

print('list of keywords in python:', keyword.kwlist)


'''
['False', 'None', 'True', '_peg_parser_', 'and', 'as', 'assert', 'async', 'await',
 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 
 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 
 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

'''



'''

a = 2 # value/object
b = 3
print(a+b)

Operators in python:
--------------------

In generally operators are used to perform some operations on values and variables.
These are standard symbols used for logical and arithmetic operations..

Operators : these are the special symbols . Eg .. + ,-,*
Operand : It is the value on which operator is applied.


Types of operators:
------------------

1.Arithmetic operator
2.Comparison operator/Relational operator
3.Logical operator
4.Bitwise operator
5.Assignment operator
6.Identity operator
7.Membership operator


1.Arithmetic operator:
-----------------------
Arithmetic operator are used to perform basic mathematical operations like addition, subtraction,
mul, division....

'''

a = 2
b = 3
print("addition", a+b)
print('sub',a-b)
print('mul',a*b)
print('div',a/b)

print('floor divison',a//b)
print('modules',a%b)
print('exponentiation', a**b) # power operator



'''
comparison operator:
-------------------
In comparison operator or relational operators compares the values. It either True
or False (Boolean expression) according to the condition...


symbol : 

== *****************

the double equals operator is used to check the right side "data", if the data is same
then it will return True other it will return False



'''

a = 10
b = 20

print(a>b)
print(a<b)

# ==

m = 22
n = 22

print(id(m))
print(id(n))

print(m == n)

print(m != n)

print(m >= n)


'''
3.Logical operator:
-----------------
The logical operators performs Logical AND, Logical OR, Logical NOT operations.
It is used to combine the conditional statements.


even the logical operators are also returning the boolean expression.

Truth table for Logical AND: If both conditions are True then the ouput is True other wise the condition is False
--------------------
T   T   T
T   F   F
F   T   F
F   F   F


Truth table for Logical OR: Atleast one condition is True then output is True
-------------------------
T   T   T
T   F   T
F   T   T
F   F   F


Truth table for Logical NOT: If the condition is True then output is False
---------------------------
T   F
F   T


0 -- False
1 -- True

'''

p = True
q = False


print(p and q)
print(p or q)
print(not p)