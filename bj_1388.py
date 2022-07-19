import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def cnt_h(x, y, arr):
    global cnt
    while True:
        if arr[x][y] == '|':
            cnt += 1
            return
        elif y == M-1:
            arr[x][y] = 0
            cnt += 1
            return
        else:
            arr[x][y] = 0
            y += 1

def cnt_v(x, y, arr):
    global cnt
    while True:
        if arr[x][y] == '-':
            cnt += 1
            return
        elif y == N-1:
            arr[x][y] = 0
            cnt += 1
            return
        else:
            arr[x][y] = 0
            y += 1

N, M = map(int, input().split())
floor = [list(input().rstrip()) for _ in range(N)]
r_floor = list(map(list, zip(*floor)))
cnt = 0

for i in range(N):
    for j in range(M):
        if floor[i][j] == '-':
            cnt_h(i, j, floor)

for i in range(M):
    for j in range(N):
        if r_floor[i][j] == '|':
            cnt_v(i, j, r_floor)

print(cnt)


