
t = int(input())
if (t < 1) and (t > 5):
    exit(0)
for x in range(t):
    dogsize = []
    sumofranges = []
    n, k = map(int, input().split())
    for y in range(n):
        d = int(input())
        dogsize.append(d)
        #print(dogsize)
        if n == k:
            print(0)
            break
    dogsize.sort()
    dogsize.reverse()
    while k > 0:
        #print('k is:',k)
        i = 0
        j = 1
        differences = []
        for z in range(len(dogsize) - 1):
            differences.append(dogsize[i] - dogsize[j])
            i += 1
            j += 1
        differences.sort()
        #print('differences:',differences)
        differences.reverse()
        if len(differences) == k:
            sumofranges.append(differences[-1])
            break
        if differences == []:
            break
        sumofranges.append(differences[-1])
        #print('sumofranges',sumofranges)
        m = 0
        n = 1
        #print('len dogsize:',len(dogsize)-1)
        #print('differences[-1]',differences[-1])
        while True:
            if (dogsize[m] - dogsize[n]) != differences[-1]:
                #print('dogsize[m]',dogsize[m])
                #print('dogsize[n]',dogsize[n])
                m += 1
                n += 1
            else:
                del dogsize[m]
                del dogsize[m]
                break
            
        k -= 1
        #print('we are at end')
        #print('dogsize',dogsize)
    print(sum(sumofranges))
            
        
        
        
