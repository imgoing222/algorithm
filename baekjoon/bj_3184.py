# 3184 양
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

# 우선 늑대찾기
def find_wolf():
    for i in range(R):
        for j in range(C):
            if yard[i][j] == 'v' and not visited[i][j]:
                count_animals(i, j)

# 울타리 안 bfs로 늑대와 양의 수 세기
def count_animals(x, y):
    Q = deque()
    # 늑대와 양 초기값
    w = 1
    s = 0
    Q.append([x, y])
    visited[x][y] = 1

    while Q:
        x, y = Q.popleft()

        dx = (-1, 0, 1, 0)
        dy = (0, 1, 0, -1)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= R or ny >= C:
                continue
            if yard[nx][ny] == '#':
                continue
            if visited[nx][ny]:
                continue

            if yard[nx][ny] == 'o':
                s += 1
            elif yard[nx][ny] == 'v':
                w += 1

            Q.append([nx, ny])
            visited[nx][ny] = 1
            
    fight_in_yard(w, s)

# 숫자 비교해서 싸우고 살아남은 동물 더해주기
def fight_in_yard(w, s):
    global sheep, wolves

    if s > w:
        sheep += s
    else:
        wolves += w


R, C = map(int, input().split())
yard = [list(input().rstrip()) for _ in range(R)]
visited = [[0]*C for _ in range(R)]
sheep = wolves = 0

find_wolf()

# 늑대가 없을 때 or 자기 영역안에 양만 있었던 곳에 있는 양의 수 더해주기
for i in range(R):
    for j in range(C):
        if yard[i][j] == 'o' and not visited[i][j]:
            sheep += 1

print(sheep, wolves)
