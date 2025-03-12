"""
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


nums_str = input("Enter numbers, seperated by comma : ")
nums_lis=nums_str.split(',')
x=int(nums_lis[0])
y=int(nums_lis[1])

mul_lis=[[0 for i in range(y)] for j in range(x)]
for i in range(0,x):
    for j in range(0,y):
        mul_lis[i][j] = i*j
print(mul_lis)


str = input("Enter words, seperated by comma : ")
lis = str.split(",")            # lis = input().split(" ") used as shortcut

for i in range(0,len(lis)):
    for j in range(i,len(lis)):
        if lis[i] > lis[j]:
            temp=lis[i]
            lis[i]=lis[j]
            lis[j]=temp
print(','.join(lis))

#or
 
lis2 = str.split(",")
lis2.sort()
print(','.join(lis2))


lis_lines=[]
while True:
    str_lines = input()
    if str_lines:
        lis_lines.append(str_lines.upper())
    else:
        break
for i in lis_lines:
    print(i)

"""

 

























