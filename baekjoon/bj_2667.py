# 2667 단지번호붙이기
import sys
sys.stdin = open('input.txt')

def dfs(x, y):
    global v

    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue

        if visited[nx][ny]:
            continue

        if house[nx][ny] == 1:
            visited[nx][ny] = v
            dfs(nx, ny)


N = int(input())
house = [list(map(int, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
v = 0

# 그림 2처럼 만들기
for i in range(N):
    for j in range(N):
        if house[i][j] == 1 and not visited[i][j]:
            v += 1
            visited[i][j] = v
            dfs(i, j)

# 아파트 단지 수
print(v)

# visited 돌면서 각 숫자별 아파트 단지 수 세기
cnt_list = []

for i in range(1, v+1):
    cnt = 0
    for r in visited:
        cnt += r.count(i)
    cnt_list.append(cnt)

for i in sorted(cnt_list):
    print(i)