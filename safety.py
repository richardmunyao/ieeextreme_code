#! /usr/bin/env python3

orig_password=input()
#print(orig_password)
ops=int(input())

to_do=[]

for x in range(ops):    
    a = [int(x) for x in input().split()]
    #print (a)
    to_do.append(a)

for y in range(ops):
    if to_do[y][0] == 1:
        i = (to_do[y][1] - 1)
        j = (to_do[y][2] - 1)
        k = (to_do[y][3] - 1)
        l=(j-i+1)

        if orig_password[i:j+1] == orig_password[k:k+l]:
            print('Y')
        else:
            print('N')

    elif to_do[y][0] == 2:
        i = (to_do[y][1] - 1)
        j = (to_do[y][2] - 1)
        k = (to_do[y][3] - 1)
        l=(j-i+1)

        new_password=orig_password[:i]+orig_password[k:k+l]+orig_password[k+l:]
        #print(new_password)
        print(orig_password[:i])
        print(orig_password[k:(k-1)])
        print(orig_password[k:])   

        
        
        

    
