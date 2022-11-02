# 4963 섬의 개수
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

def bfs(x, y):
    Q = deque()
    Q.append([x, y])

    while Q:
        x, y = Q.popleft()

        dx = (-1, 0, 1, 0, -1, 1, 1, -1)
        dy = (0, 1, 0, -1, 1, 1, -1, -1)
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                continue

            if board[nx][ny] == 1:
                Q.append([nx, ny])
                board[nx][ny] = 0


while True:
    w, h = map(int, input().split())
    ans = 0
    
    if w == 0 and h == 0:
        break
    else:
        board = [list(map(int, input().split())) for _ in range(h)]

        for i in range(h):
            for j in range(w):
                if board[i][j] == 1:
                    bfs(i, j)
                    ans += 1

    print(ans)
    