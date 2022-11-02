# 9205 맥주 마시면서 걸어가기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

def bfs(x, y):
    Q = deque()
    Q.append([x, y, 0, 19])
    visited.append([x, y])

    while Q:
        x, y, d, beer = Q.popleft()
        
        if [x, y] in store:
            beer = 19

        if d + 1 == 50:
            if beer:
                beer -= 1
                d = 0
            else:
                print('sad')
                return

        if [x, y] == festival:
                print('happy')
                return

        dx = (-1, 0, 1, 0)
        dy = (0, 1, 0, -1)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if [nx, ny] not in visited:
                Q.append([nx, ny, d+1, beer])


t = int(input())
for _ in range(t):
    n = int(input())
    home = list(map(int, input().split()))
    store = [list(map(int, input().split())) for _ in range(n)]
    festival = list(map(int, input().split()))
    visited = []

    bfs(home[0], home[1])