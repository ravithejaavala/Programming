# 20-02-25
'''

nested flow controls:
---------------------------

nested if statement

nested if elif statements

nested if elif elif statements

nested if elif else statements


nested if statement:
-------------------
A nested if statement in python is an if statement located within another if or
else clause...


syntax:
----

if condition(expression): (main condition)
    # block of statements

    if condition:(nested condition)
        # block of statements


Notes:
----
If main condition is True then only the block of statements and nested condition will
check otherwise it won't check.

If it in case the main condition is False, then it will be comes out the condition..

If we are defining any variable under the Main condition then we are able to access
those variables in the nested function as well.

But if you are defining any variable under the nested function then we are able acces inside of the nested function but not
in the main function.


'''

num = 34

if num == 34: # main condition
    print('--main if condition----')
    name = 'sai kiran'
    if num > 20: # nested if condition
        print('--nested if condition---')
        print('34 is greater than 20')
        print('--name---',name)
        age = 28
        if len(name) > 3: # inner most if condition
            print('inner most condition')
            print(age)


'''
nested if elif else statement:
-------------------------

if condition:
    # block of statements

elif condition:
    # block of statements
    if condition:
        # block of statements
    elif condition:
        # block of statements
    else:
        # block of statements
else:
    # block of statements
print()
'''

# nested if elif else statement

i = 77

if i != 77:
    print('77 is not equal to 77')
elif i > 50 and i == 77:
    print('--main elif condition---')
    if i > 80:
        print('77 is not greater than 80')
    elif i > 25:
        print('--nested elif condition---')
        print('77 is greater than 25')
    else:
        print('--nested else block----')
else:
    print('--main else statement--')
print('')


'''
nested if elif else statements:
----------------------------

syntax:
----

if condition:
    # block of statements
elif condition:
    # block of statements
else:
    if condition:
        # block of statements
    else:
        # block of statements

'''

# nested if elif else statements

p = 2
q = 3

if p > q:
    print('p is not greater than q')
elif p == q:
    print('p is not equals to q')
else:
    print('--main else block----')
    if p > q and p == 2:
        print('p is equals to 2 but p is not greater than 3')
    else:
        print('--nested else block---')
        print('completed!!')

'''
loops


for loop
while loop

'''