"""
a = 2000
b = 3200
l=[]
for i in range(a, b+1):
    if i%7 == 0 and i%5 !=0:
        l.append(str(i))

print(','.join(l))


num= int(input("Enter number : "))

def fact(num):
    res = 1
    if num==0:
        return res
    '''for i in range(1,num+1):
        res= i*res'''
    res = num*fact(num)
    return res
print("factorial",fact(num))


num = int(input("Enter a number : "))
d3={}
for i in range(1, num+1):
    d3[i] = i*i
print(d3)



seq = input()

list1 = seq.split(',')

tup=tuple(list1)

print(list1)
print(tup)

list1.sort(reverse=True)
 
print(list1)



# getString: to get a string from console input
# printString: to print the string in upper case.


class two():
    self= ""
    def getString(self):
        self.s1=input("Enter : ")
    def printString(self):
        print(self.s1)



st = two()

res1=st.getString()
res2=st.printString()


import math

C = 50
H = 30.
inp = input()


l=inp.split(",")
res_li=[]
for i in l:
    D=int(i)
    #Q = ((2 * C * D)/H)**(1/2)
    Q = math.sqrt((2 * C * D)/H)
    res_li.append(round(Q))
print(res_li)

l= ["1", "2", "3", "4"]
print(','.join(l))

"""""

x = int(input("Enter X value : "))
y = int(input("Enter Y value : "))
res_lis=[[0]*y]*x
for i in range(0,x):
    for j in range(0,y):
        res_lis[i][j] = i*j
    print(res_lis)

print(res_lis)




































