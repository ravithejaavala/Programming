# !8-02-25
'''

4.Assignment operator:
---------------------
In python , the asssignment operators are used to assign values to the variables.
This operator is used to assign the value of the right side of the expression to the
left side operand..



'''

a = 1
b = a

print(b)

b += a # b = b+a

print(b)

b -= a # b = b-a

print(b)

b *= a
print(b)


'''
identity operator:
-----------------
In python, "is" and "is not" are the identity operators both are used to check if the two
values are located on the same part of the memory or not.

So if the objects/values are pointing to the same object then the "is" operator is
return True otherwise return False

is        : If the operands are identical then it will return True
is not    : If the operands are not identical then it will return True


mutable / immutable


'''

name = 'sarath'
name1 = 'sarath'

print(name is name1)


li = [1,2,3]
li1 = [1,2,3]

print(id(li))
print(id(li1))

print(li is not li1)


'''
Membership operator:
-------------------
In python , "in" and "not in" are the membership operators that are used to test
whether a value or variable is in a sequence.

in     - If the value is found in the sequence then it will return True
not in - If the value is not found in the seq then it will return True

'''

a = 9
b = 3

li = [1,2,3,4,5,6]

if b in li:
    print('3 in list')
else:
    print('3 is not in the list')


if a not in li:
    print('9 is not in sequence')
else:
    print('9 is in seq')


'''
Ternary operator:
-----------------
In python, ternary operators also know as conditional expressions are operators that
evaluate something based on a condition being True or False. In this operator, we can
write conditions in a single line..


'''


a,b = 30,40

min_val = a if a < b else b
print(min_val)



'''
Bitwise operator:
---------------
Python bitwise operators act on bits and perform bit by bit operations. These are
used to operate on binary numbers.

Bitwise and (&)
Bitwise or (|)
Bitwise not (~)


Bitwise and (&):
------------

a = 10
b = 4


a = 0 1 0 1

a = 1 0 1 0 (bottom to up)

b = 0 0 1 

b = 0 1 0 0 (bottom to up)


a&b: (and)

1 0 1 0
0 1 0 0
---------
0 0 0 0 = 0


a|b:
---


1 0 1 0
0 1 0 0
---------
1 1 1 0
8+4+2+0 = 14      


Bitwise not(~):
----------------

a = 10

1 0 1 0


1's compliment
2's compliment


sign bits : ~0 = 1  +ve numbers
            ~1 = 0   -ve numbers

0   1 0 1 0
------------
1   0 1 0 1  --- 1's compliment


-ve numbers are stored in the form of 2's compliment:
    --> just fliping the 1's compliment
    --> 2's compliment : add 1 to the 1's compliment

1   0 1 0 1
-----------
1   1 0 1 0
         + 1
-------------------
1    1 0 1 1
1    8+0+2+1 = -11



    


'''
a = 10
b = 4
print(a&b)

print(a|b)

print(~a)