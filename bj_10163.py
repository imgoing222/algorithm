import sys
sys.stdin = open('input.txt')

board = [[0]*1001 for _ in range(1001)]
N = int(input())

for i in range(1, N+1):
    x, y, w, h = map(int, input().split())
    for j in range(y, y+h):
        for k in range(x, x+w):
            board[j][k] = i
    
for i in range(1, N+1):
    cnt = 0
    for j in range(1001):
        for k in range(1001):
            if board[j][k] == i:
                cnt += 1
    print(cnt)

        




