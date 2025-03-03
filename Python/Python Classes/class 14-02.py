'''

Python:
------

python vs java therotical wise both same....


sytnax wise is different...

Python is a high level of programing language, interpreted programing language, dynamically
typed programing language...


Founder of python Guido van Rossum in 1991...

java introduced on 1995...


python : web applications - facebook, instagra,phone pe, g pay, youtube....

python version : 1.x, 2.x and 3.x

1.x, 2.x - so many disadvatnage

3.x -- too many advantages .... too built in libraries, modules, packages....

python:
---------
a = 9
b = 9
print(a+b)


example of java adding two numbers:
------------------

import java.io.*;
{
public static void main()
{
int a = 8;
int b = 8;
int c = a +b;
system.out.println(c);
}
}


what we can do with the python?
---------------
1. Web development - Flask, Django & fastapi   *********
2. Data science and ML and AI - pandas, numpy, Tensor flow... *****
3. Automation and scrpting : ************
4. DevOps and cloud : Automation script and api's  ************


job?
3 years exp atleast...





'''

print("hello all!!")

a = 9
b = 9
print(a+b) 

'''

Python introduction:
------------------

Python is a high level programming, interpreted programming lan, dynamically typed
programming lan...


high level programming:
----------------------
High level programming language which is nothing but the normal humans could able to
understand the syntax or the noraml peace code then we can say that the languages are
low level lan....

ex: python

low level : the machine only able to understand the logic then we can consider those lan
are low level languages.

ex : c

dynamically typed programming language: ****************
-----------------------------------
In python, we don't need to specify or declare the type of variable because it is a
dynamically typed programing language..

n = 9 # value/object

name = 'siva' # value/object

Intrepreter is always intrested into the RHS side.. based on the RHS the interpreter identify
that what type of value/object it is...(int, str, list)...



interpreted programming language:
----------------------------------

An interpreted programing language is type of programming that executes instructions
directly, without first compiling them into the machine code.
the code is translated and executed line by line process....






'''

name = 'dinesh' # value / object
print(name)


string= 'hello all'
print(string)

a = 9
b = 99
print(b-a)


'''
Features in python:
---------------------

Free and open source:
------------
Python language is freely available at the offical website and we can download it from the
give download link...


Easy to code:
-----------
Python is a high level programming language (which means we don't want to take care of
the memory management) .
Python is very easy to learn the language as comparted to other languages like c, java...
It is very easy to code and easy to understand python syntax... Finally python is a
developer friendly language...


Easy to Read:
-------------
Python's syntax is really straight forward, the code block is defined by the indentations
rather than the semicolon or brackets...

Object oriented programming language: ***********
---------------------------------
Basically python supports oops and concepts of classes, object and encapsulation...


High level language:
-------------------

Python is a high level prorgaming lan, we don't need to remember the system architecture
and we don't need to manage the memory as well...


Easy to Debug:
-------------

Information for mistake tracing and we need to able to quickly identify and correct
the issues and we have too many built in libraries to debug the issue. So one of the module
is ::: pdb -- **************

pdb.set_trace() - real time




'''

name = 'sai kiran' '''

key features in python:
---------------------------
Portable language:
--------------
If we have python code for windows and if we want to run this code on other platforms
such as linux, unix and mac then we don't need to change it, we can run this code on any
platform...


Interpreted language: ********
--------------------
Python is an interpreted language because it executes the peace of code line by line at
a time. there is no need to compile the code this makes it easier to debug our code.
The source code in python is converted into an immediate form called "bytecode"

nam = 'sarath'


Large standard library:
------------------------
Python has a large standard library that provides a rich set of modules(.py) and functions
so you don't have to write the own logic code for every single thing...


example : math, re, boto3, os, sys, print()


Dynamically typed programing:
---------------------------
python is a dynamically typed programing lan. That means the type for (int,str, list)
 for a variable is decided at the "run time"  not in advance because of this feature
 we don't need to specify the type of the variable..


Allocating Memory dynamically:
--------------------------

the variable data type does not need to be specified. THe memory is automcatically
allocated to a variable at runtime when it is given a value...

name = 'dinesh'



'''

import math

print(math.sqrt(9))



'''
Memory Management in python:
-----------------------
Memory allocation can be defined as allocating a block of space in the computer
memory to a program. In python memory allocation and de allocation method is automatic
as "garbage collector" for python that the user does not have to do the manual 
garbage collection...


Garbage collection:
------------------
Garbage collection is a process in which the interpreter frees up the memory when not
in use to make it available for other object..

Assume a case where no reference is pointing to an object in memory i.e ,. it is not in
use so, the virtual machine(interpreter) has a garbage collector that automcatically
deletes that object from the memory(heap memory)...


Reference counting:
-----------------
Reference counting works by counting the number of times an object is referenced by
the other objects in the system. When the references to an object are removed,
the reference count for an object is decremented. When the reference count becomes zero,
the object is deallocated...


'''


name = 'sarath'

print(name)



a = 9
b = a

print(a)
print(b)

print(id(a))


x = 10
y = x
x = x+1

print(x) # 11

print(y) # 10




