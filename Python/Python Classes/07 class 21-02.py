'''


loops:
----
In python, the loops are used to repeat actions effiectively... If we want to iterate
the data then we need to use the loops.

We have two types of loops:
1. While loop
2. For loop


While loop:
----------
While loop is used to execute the block of continuesly until some condition becomes
meet.

----or----
While loop is used to execute the block of statements repeatedlty until a given
condition is satisifed. When the condition becomes false, the line immediatly
after the loop in the program is executed....

syntax:
----

while expression(condition):
    # block of statements

------


while expression(condition):
    # block of statements
else:
    # block of statements

'''

# example - 1

i = 0

while i < 3:
     i += 1 #i = i +1
     print('hello all')



# example  - 2


a = 1

while a < 5:
    a += 2
    print('sarath')
else:
    print('while loop else block')

# example - 3

p = 0

while p < 4:
    p += 3
    print('done')

'''
nested while loop:
---------------


while condition: # main loop
    # block of statements
    while condition: # nested loop
        # block of statements

x = [1,2]
y = [4,5]


1 4
1 5
2 4
2 5


'''
x = [1,2]
y = [4,5]

i = 0
while i < len(x):
    j = 0
    while j < len(y):
        print(x[i], y[j])
        j += 1
    i += 1
else:
    print('--main else block in while loop---')