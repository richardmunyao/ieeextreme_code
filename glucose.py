x = input().split()
x = list(map(int,x))
c = x[0]
h = x[1]
o = x[2]
if c < 0 or h < 0 or o < 0:
    print('Error')
if c > pow(10, 10) or h > pow(10, 10)  or o > pow(10, 10):
    print('Error')
else:
    if ((2 * o) - h) % 4 > 0:
        print('Error')
    else:
        r = ((2 * o) - h) // 4
        q = (o - c) - r
        s = (h - (2 * q)) // 12
        if r < 0 or q < 0 or s < 0:
            print('Error')
        else:
            print(q, r, s)
