# 2178 단지번호붙이기
import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

def bfs(x, y, cnt):
    Q = deque()
    Q.append([x, y, cnt])
    visited[x][y] = 1

    while Q:
        x, y, cnt = Q.popleft()
        dx = (-1, 0, 1, 0)
        dy = (0, 1, 0, -1)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if visited[nx][ny]:
                continue

            if maze[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                Q.append([nx, ny, cnt+1])



N, M = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

bfs(0, 0, 1)

print(visited[N-1][M-1])