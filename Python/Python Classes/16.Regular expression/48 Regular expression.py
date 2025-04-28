# 25-04-25

'''

Regular expression:
--------------------

A regular expression or RegEx is a special sequence of characters that uses a search
pattern to find a string or set of strings...

It can detect the presence or absence of a text by matching it with a particular
pattern and also can split a pattern into one or more sub patterns...

Python has a built in module named "re" that is used for regular expressions. We can
import this module by using the import statement..


'''

import re

txt = 'hello all good evening!!'
match = re.search(r'all',txt)
print(match.start())
print(match.end())

'''

re.findall()
re.compile()
re.split()
re.search()

re.findall():
-----------

Return all non overlaping matches of pattern in string, as a list of strings. The
string is scanned left to right and matches are returned in the order found

'''

txt = 'Hello Dinesh my phone number is 435678756 and another number is 454635345345'
regex = '\d+'
match = re.findall(regex, txt)
print(match)


'''
re.compile()
-----------
Regular expressions are compiled into pattern objects, which have methods for various
operations such as searching for pattern matches or performing strng substitutions..

'''

com = re.compile('[a-k]')
print(com.findall('hello all good evening!!'))


'''
re.split():
-------
split string by the occurence of a character or a pattern, upon finding that pattern,
the remainig charcters from the string are returned as part of the resulting list

'''

from re import  split

print(split('\W+','sarath, dinesh,ravi'))

'''
Meta characters:
---------------
[]      -   Represent a character class
^       -   Matches the beginning
$       -   Matches the end
.       -   Matches any character except newline


[] - square brackets:
------------------
Square brackets[] represents a character class consisting of a set of characters that
we wish to match...

'''

txt = 'python programming language'
patt = '[a-f]'
res = re.findall(patt, txt)
print(res)

'''
^  - Caret:
-----------
Caret(^) symbol matches the beginning of the string i.e ,, checks whether the string
starts with the given character or not...

'''

regex = r'^p'
string = ['python', 'programming', 'language']
for i in string:
    if re.match(regex, i):
        print(f'Matched:{i}')
    else:
        print(f'Not Matched:{i}')


'''
$ - Dollar:
---------------
Dollar($) symbol matches the end of the string i.e. checks whether the string ends
with the given characater or not..

'''


string = 'Hello world'
pattern = r'rld$'

match = re.search(pattern, string)
if match:
    print('Match found')
else:
    print('Match not found')