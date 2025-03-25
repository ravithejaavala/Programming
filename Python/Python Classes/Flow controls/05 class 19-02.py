'''

Flow controls/Decision making:
-----------------------------
In python, if-else is a fundemental condition statements which are used for the decision
making in programing. It allows us to execute the block of statments or block of code
depending on the condition is True or False.


if statement

if else statement

if elif else statement

if elif elif else statement

nested if statement

nested if else statement

nested if elif else statement

nested else statement



if statement:
------------
If statement is the most simple decision making statement. If the condition evalutes
True, the block of code inside the "if statement" is executed.


syntax:
-------

if statement(condition): # indentation
    # block of statement / block of code (when condition is True)

# this block will execute (when condition fails)


'''

# if statement

i = 4
if i > 3:
    print('---inside if condition----')
    print('4 is greater than 3')

print('completed!!!') # doesn't comes under the if condition


'''
if else statements:
--------------------
if condition is True then it will execute the if block of statements otherwise it
will come into the else and execute the block of statement

if condition:
    # block of statements
else:
    # block of statements



'''

num = 22

if num > 5:
    print('In the main if condition')
    print('22 is greater than 5')
else:
    print('Inside the else condition')
    print('22 is not greater than 5')
print('')


'''
if elif else statements:
----------------------

if condition : If condition is True , then it will execute block of statements and it won't
                read the reamingin statements.
elif condition : the first "if condition" fails then only it will come into the elif
                condition and then it will execute the block of statements
else          : both if and elif conditions are fails, then the else block directly
                will execute the statements


if condition:
    # block of code
elif condition:
    # block of code
else:
    # block of code


'''

name = 'sai kiran'
num = 7
if len(name) > 10:
    print('--------if cond ----------')
elif len(name) > 5 and num > 4:
    print('-----elif condition---------------')
    print('7 is greater than 4 and name is having more than 5 characters')
else:
    print('--else block--')



'''
if elif else statements:
----------------------

if condition : If condition is True , then it will execute block of statements and it won't
                read the reamingin statements.
elif condition : the first "if condition" fails then only it will come into the elif
                condition and then it will execute the block of statements
elif condition : both if condition and elif condition are fails then only it will execute
                the second elif condition ..
else          : both if and elif conditions are fails, then the else block directly
                will execute the statements


if condition:
    # block of code
elif condition:
    # block of code
elif condition:
    # block of code
else:
    # block of code
print()

'''

a = 3
b = 4

if a == 5 and b > 3:
    print('--if condition----')
elif a > 7 or b == 3:
    print('---first elif condition----')
elif a == 3 and b > 2:
    print('---second elif condition----')
    print('a is equals to 3 // 4 is greater than 2')
else:
    print('---else block---')
print('')