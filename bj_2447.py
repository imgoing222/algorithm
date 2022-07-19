def star(N, x, y):
    if N == 3:
        arr[x+1][y+1] = ' '
        return
    else:
        while True:
            
        

N = int(input())
arr = [['*']*N for _ in range(N)]
star(N, 0, 0)

for i in range(N):
    for j in range(N):
        print(arr[i][j], end='')
    print()