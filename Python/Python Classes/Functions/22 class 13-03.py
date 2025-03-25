'''
Functions:
---------


def function_name(parameters):
    # block of code
function_name(arguments) -- calling

# docstring:
----
The firsr string after the function is called the Document string or docstring.
This is used to describe the functionality of the function. The use of docstring in functions
is optional but it is considered as a good practice..

def fun():
    'fun'
    # block of code

fun()


'''

def add(a,b):
    '''adding the two numbers'''
    return a+b
print(add(1,2))
print(add._doc) # __doc_  --- Magic methods / dunder methods / special methods

'''
Types of function arguments:
--------------------------

1. Default arguments
2. Keywor arguments
3. Positional arguments
4. Arbitrary arguments (variable length argument)


Positional arguments:
-----------------------
When the function call statement must match the number and order of argumetns as defined
in the function definition ,then we can consider as positional arguments

'''


def wish(name, age, sal):
    '''person details'''

    print("name:",name, 'age:',age, 'sal:',sal)

wish('dinesh',27,325346)


'''
Default arguments:
---------------
A default argumetn is a parameter that assumes a default value if a value is not provided
in the function call for that argument...


'''


def display(a,b,c=0):

    print(a,b,c)
display(1,2)


def fun(x,y=22,z=33):

    print(x,y,z)

fun(11)



def wis(a=0,b=1,c = 2):
    print(a,b,c)
wis(1)


'''

Keyword arguments:
-------------------
using the keyword arguments, the argument passed in the function call is matched with the
function definition on the basis of the name of the parameter

'''


def emp_details(emp_name, emp_age, off_loc):
    print(emp_name, emp_age, off_loc)

emp_details(off_loc='blr',emp_name='hyma',emp_age=29)
emp_details('sarath',off_loc='hyd',emp_age=30)


'''
Arbitrary keyword arguments/variable length argument:
------------------------------------------
*args , **kwargs can pass a variable 'n' number of arguments to a function using the special
symbols.

*args     - Non - keyword arguments
**kwargs  - keyword arguments


'''

# *args     - Non - keyword arguments

def myfunc(*args):
    for i in args:
        print(i)

myfunc(1,2,3,'sarath','dinesh','sai')



# **kwargs  - keyword arguments


def func(**kwargs):

    for k, v in kwargs.items():
        print('%s == %s' %(k,v))
func(first_name='sarth',last_name='k',age='30',sal=45678,gender=435678)