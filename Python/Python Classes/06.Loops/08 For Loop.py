#22-02-25
'''

loops:
----


for loop:
-------

Python For loops are used for iterating over a sequence like lists, tuple, dict....

if input is not in sequence then for loop don't work ..

synatx:
-----

for var in input:
    # block of statements


'''


li = [1,2,3,4]

for i in li:
    print(i)


name = 'sai kiran'

for i in name:
    print(i)
else:
    print('--else in for loop--')


# in which for loop doesn't work


# num = 23
#
# print(type(num))
#
# for i in num:
#     print(i)


# nested for loop

x = [1,2]
y = [4,5]

for i in x:
    for j in y:
        print(i, j)


'''
break
pass
continue

break:
-----
The break statement in python, is used to exit or break out of the loop (either
for loop or while loop) , before the loop has iterated all its items or reached
its condition. When the break statement is executed, the program immediately exists
the loop, and control moves to the next line of the code after the loop..


syntax:
--

for var in inp:
    # statement
    if cond:
        break
'''

for i in range(0,10):
    print(i)
    if i == 6:
        break


name = 'sai kiran'

for i in name:
    if i == 'r':
        break
    print(i)


'''
continue statement:
------------------
Continue statement is a loop control statement that forces to execute the next
iteration of the loop while skipping the rest of the code inside the loop for the
current iteration.

Python continue statement skips the execution of the program block after that the
continues statement and forces the control to start the next iteration...


for i in in:
    # statement
    if con:
        continue


pass statement:
----------
Pass statement in python is a null operator . It is used when a statement is syntactically
required but we don't want to execute the statements or code..

for i in range(0,10):
    pass
  
'''


for i in range(0,7):

    if i == 4:
        continue
    print(i)


for i in range(9):
    pass


i = 4

while i < 7:
    pass

def sample():
    pass

class Emp:
    pass

'''

data types:
----


'''