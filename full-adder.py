#! /usr/bin/env python3

in_line1 = input()
line1 = [f for f in in_line1.split()]
base=int(line1[0])
if base < 2 or base > 62:
    exit()
symbols=list(line1[1])

mapper={}

for x in range(base):
    mapper[(symbols[x])]=x


zero = [key for key, value in mapper.items() if value == 0][0]


in_param1 = input()

param1=in_param1.strip()
param1=list(param1)

in_param2 = input()
param2=in_param2.strip()
param2=param2.strip('+')
param2=param2.strip()
param2=list(param2)

junk1=input()
junk2=input()

len_param1=len(param1)
if len_param1 > pow(10,7):
    exit()
len_param2=len(param2)
if len_param2 > pow(10,7):
    exit()
len_diff=len_param1-len_param2

if len_diff < 0:
    for pd in range(abs(len_diff)):
        param1.insert(0, zero)
elif len_diff > 0:
    for pd in range(abs(len_diff)):
        param2.insert(0, zero)

param1.reverse()
param2.reverse()


ansb4=[]
ansafter=[]
carry=0
for lp in range(len(param1)):
    
    temp=mapper[param1[lp]] + mapper[param2[lp]]+carry
    
    if temp>=base:
        f=temp-base
        ansb4.append(f)
        carry=1
    else:
        
        ansb4.append(temp)
        carry=0

ansb4.reverse()

for trans in ansb4:
    lb = [key for key, value in mapper.items() if value == trans][0]
    ansafter.append(lb)

print(in_line1)
print(in_param1)
print(in_param2)
print(junk1)

print('',''.join(ansafter))
