# 28-02-25
'''
string methods:
---------------

# encode() : this method returns an encoded version of the given string

'''

nam = 'sarath'
print(nam.encode())

# endswith() : this method return True if a string ends with the specified suffix, if not it returns False

msg = 'python as a lan'
print(msg.endswith('lan'))

#expandtabs() : this method takes an integer argument and the default size is 8 and  used \t characters


names = 'sarath\tdinesh\thyma'
print(names.expandtabs(2))


#find() : ***************
#  this method returns the index of first occurence of the substring (if found),
# if not found, it returns -1.

name = 'python is an awesome'
print(name.find('an'))
print(name.find('z'))

# index() : ***********
# this method returns the index of a substring inside the string if it found.
# if the substring is not found in the main string then it raises an exception(ValueError)

txt = 'python is good'
res = txt.index('d')
print(res)
# res = txt.index('q')
# print(res)


# format() : this method allows the use of simple placeholders for formatting.


print('Hi {}, your account balance is {}'.format('sarath',3456843)) # default arguments

print('Hi {1}, your account balance is {0}'.format('sarath',3456843)) # positional arguments

print('Hi {name}, your account balance is {bala}'.format(name = 'sarath',bala = 3456843)) # keyword arguemnts

print('Hi {}, your account balance is {balan} and your age is {age}'.format('dinesh',balan = 34563, age = 26)) # mixed arguments

print("the number is {:d}".format(123))

# {0:f} - float, {0:bin} - binary , {0:x} - hexadecimal

#isalnum() : THis mehtod returns True, if all characters in the string are alphanumeric
# , if not it returns False

txt = 'python 3'
print(txt.isalnum())


#isaplha() : This method returns if all characteres in the strings are alphabets(
# it can be both lower case and upper case) and it returns False at leat one character
# is not alphabet


txt = 'python'
print(txt.isalpha())

#isupper() : this method returns True, if all characters in a string are upper case
# it returns False, if any characters in a string are lower case characters

name = 'SAI'
print(name.isupper())

#islower()

# join() **************
# this method returns a string by joining all the elements of an iterable(list,
# string, tuple) ,separated by the given separator..
names = ['sarath','reddappa','sai']
print(type(names))

sep = ':'.join(names)
print(type(sep))
print(sep)


# lower() : this method converts all upper case characters in a string to lower case

msg = 'Hello WorlD!!'
print(msg.lower())

# upper() :

msg = 'Hello WorlD!!'
print(msg.upper())

#isupper()

msg = 'HELLO WORLD!!'
print(msg.isupper())

#islower()


# replace() : *********
# this method replaces each matching occurence of a substring with another string

name = 'sarath'
repl = name.replace('a','b',1)
print(repl)

# split() : this method breaks a string into a list of substrings ...

text = 'sarath hyma siva'
print(text.split())


# strip() : this method removes the empty spaces from both the sides

msg = '        hello         '

print(msg.strip())
print(msg.lstrip())
print(msg.rstrip())

# swapcase() : it converts all the characters to their opposite letter case

name = 'SaraTH'
print(name.swapcase())