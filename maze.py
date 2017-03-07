matrix = []
counter = 0
side = int(input())
for y in range(side):
    matrix.append([])
    for z in range(side):
        matrix[y].append('x')
while True:
    af = [int(f) for f in input().split()]
    a=af[0]
    
    if a == -1:
        break
    b=af[1]
    matrix[a - 1][b - 1] = 'o'
    counter += 1
matches = 0
for column in range(side):
    for row in range(side -1):
        if matrix[row][column] == matrix[row + 1][column] == 'o':
            matches += 1
if matches == (side - 1):
    print(counter)
else:
    print(-1)
    




