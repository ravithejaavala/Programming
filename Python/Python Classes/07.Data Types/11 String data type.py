# 27-02-25
'''

string data type:
----------------
String is an immutable data type. So once we create the data , we can not able to
change or modify.

C R U D operations:

C - create
R - retrieve
U - update
D - delete

Strings are amongst the most popular data type in python. We can create the string
by using the single or double quotes and even for triple quotes. In python there
is no character data type, hence even single character also consider as a string
data type only.

----------or---------------------
A string is a sequence of characters. In python treats anthing inside quotes as
a string. This includes letters, numbers, and symbols. In python there is no
character data type so single character is a string data type and length of 1.



name = 'sarath'

gender = "male"

text = """I learnig python from basics"""

m = 'a'

'''

# create operation

name = "dinesh123" # create
print(type(name))

print(name)

# retreive operation

print(name[2]) # 2 represents the index


for i in name:
    print(i)

# update operation

name = 'sarath' # bharath
# name[0] = 'bh'
print(id(name))

# by using the concatenation

name = 'bh' + name[1:] # bharath
print(name)
print(id(name))


# delete operation

name = 'bharath'
del name
# print(name)

### string methods


# capitalize() : this methods converts the first character of a string to an upper
# case letter and all the other characters to lower case

name = 'HyMA sReE'
res = name.capitalize()
print(res)

# casefold() : this method converts all characters of the string into the lowercase
# letters and returns a new string.

name = 'HyMA sReE'
res = name.casefold()
print(res)

# center() : this method returns a new centered string after padding it with the
# specified character.

nam = 'hyma sree'
new_string = nam.center(24, '*')
print(new_string)


# count() : this method returns the number of occurences of a substring in the given string

msg = 'python programming'
print(msg.count('z'))