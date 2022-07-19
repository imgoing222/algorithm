import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def is_not_valid(a, b):
    if adj[a][b] and not visited[b]:
        visited[b] = 1
        return 0
    return 1

L = int(input())
A = list(map(int, input().split()))

adj = [[1] * 10 for _ in range(10)]
li = [[1, 3], [1, 7], [1, 9], [2, 8], [3, 7], [3, 9], [4, 6], [7, 9]]
visited = [0] * 10
visited[A[0]] = 1

for i in range (len(li)):
    adj[li[i][0]][li[i][1]] = 0
    adj[li[i][1]][li[i][0]] = 0
    adj[i][i] = 0

for j in range(L):
    if A[j] == 2:
        adj[1][3] = 1
        adj[3][1] = 1
    elif  A[j] == 4:
        adj[1][7] = 1
        adj[7][1] = 1
    elif A[j] == 5:
        adj[2][8] = 1
        adj[8][2] = 1
        adj[1][9] = 1
        adj[9][1] = 1
        adj[3][7] = 1
        adj[7][3] = 1
        adj[4][6] = 1
        adj[6][4] = 1
    elif A[j] == 6:
        adj[3][9] = 1
        adj[9][3] = 1
    elif A[j] == 8:
        adj[7][9] = 1
        adj[9][7] = 1
    
    if j == 0:
        pass
    else:
        if is_not_valid(A[j-1], A[j]):
            print('NO')
            exit()

print('YES')