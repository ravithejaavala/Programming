'''
name = 'dinesh' # value = object
print(name)



a=1 
b=a

# here one object and two references


l=[1,2,3,4,5,6,7,8,9,0]

for i in l:
    if i==7:
        print("pass")
        pass
    else:
        print(i,end="")
    print(" Ravi teja")


name="raviteja"
print(name.replace('a','q',2))

l= [1,8,3,6,5]
l2=["ravi", "teja", "raju"]
#l.insert(5,4)
res=min(l)
print(l)
print(res)

nam = 'hyma sree'
new_string = nam.center(24, '*')
print(new_string)

name = 'sarath'
repl = name.replace('a','b',2)
print(repl)


name = "Ravi Teja Redy"
print(name.split())

import copy
l= [1,8,3,6,8,["ravi", "teja", "raju"]]

res=copy.copy(l)
print(res[0])
res.reverse()

print(l)
print(res)



tup = ("ravi", "teja", "raju")
l= (1,8,3,6,8,["ravi", "teja", "raju"])
print(type(tup))

l[5][2]=["ravi"]
print(l)

for i in l:
    print(i)

    '''
# ==========   Dictnory =========

'''
d2.clear()
d2.copy()
d2.fromkeys()
d2.get()
d2.items()
d2.keys()
d2.values()
d2.update()

d2.pop()
d2.popitem()
d2.setdefault()
'''
'''
# one 'key : value' pair is known as one item
d1= {'fname' : 'Ravi', 'mname' : 'Teja', 'age' : 20, 'sname' : 'Avala', 'lname' : 'Reddy'}

print(d1)




d2 = {'list' : {1:'one',2:'two',3:'three'}}
print(id(d1))
print(id(d1['fname']))

res = d1 .get('fname') # if key is not in the given dictnory, it returns 'None'
print(res)

numbers = {1,2,3}

values = "int"

d3 = dict.fromkeys(values, numbers)
print(d3)



d4= {'fname' : 'Ravi', 'mname' : 'Teja', 'age' : 20, 'sname' : 'Avala', 'lname' : 'Reddy'}

res= d4.popitem("fname")
print(res)




set2=set()

print(type(set2))

set1={1,2,3,4,5}


tup = ("ravi", "teja", "raju")

set2={3,4,5,6,7,8,9,0}
set1 &= set2

print(set1)

'''
x=3
y=5
l= [[0 for col in range(5)] for row in range(3)]
res_lis=[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
for i in range(0,x):
    for j in range(0,y):
        res=res_lis[i][j] 
        #print(res)
print(l)