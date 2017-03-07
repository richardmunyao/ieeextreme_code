pile_sizes=[]
testcases=int(input())
for b in range(testcases):
    no_of_games=int(input())
    for a in range(no_of_games):
        piles=int(input())
        results=input()
        pile_sizes.append(results)
    
if testcases == 1:
    print('Alice')
    
if testcases%2==0:
    print('Alice')
    print('Bob')

if testcases>2:
    for x in range(testcases-1):
        print('Alice')
        print('Bob')
