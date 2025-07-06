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



lis = input().split(" ")
lis.sort()
res=[]
for i in lis:
    if i not in res:
        res.append(i)
print(' '.join(res))

# or 


lis = input().split(" ")
set1 = set(lis)
lis2=list(set1)
lis2.sort()
print(' '.join(lis2))



inp = input()
lis= inp.split(",")
res=[]
for i in lis:
    num=0
    k=3
    for j in range(4):
        num=num+int(i[j])*(2**k)
        k-=1
    if num%5==0:    
        res.append(num)
res2=[]
for num in res:
    temp_lis=[0,0,0,0]
    k=3
    for j in range(4):
        if num == 0:
            temp_lis[j]='0'
        elif num >= 2**k:
            temp_lis[j]='1'
            num=num - 2**k
        else:
            temp_lis[j]='0'
        k-=1
    res2.append(''.join(temp_lis))

print(','.join(res2))


"""

# str = input()
# str1=str
# li = str1.split(",")
# print(li)

# li2 = list(map(int, str.split(',')))

# li3=list(li2)
# print(li3)


# def wish(n):

#     return n % 2 == 0
# n = [1,2,3,4,5] # global variable
# res = filter(wish, n)

# print(type(res))

# print(list(res))

# lis = [[1,2,3],[4,5,6],[7,8,9]]

# nest_list_com = [j for i in lis for j in i]
# print(nest_list_com)
