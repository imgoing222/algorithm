# 14503 로봇 청소기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(100000)

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)
def cleaning(x, y, d):
    global flag

    if flag:
        # 현재 위치 청소
        visited[x][y] = 1

    cnt = 0

    while cnt < 4:
        d -= 1

        if d < 0:
            d += 4

        nx = x + dx[d]
        ny = y + dy[d]

        cnt += 1

        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue

        if visited[nx][ny]:
            continue
        
        
        if area[nx][ny] == 0 and not visited[nx][ny]:
            flag = 1
            cleaning(nx, ny, d)

    if d < 2:
        nx = x + dx[d+2]
        ny = y + dy[d+2]
    else:
        nx = x + dx[d-2]
        ny = y + dy[d-2]

    if nx < 0 or ny < 0 or nx >= N or ny >= M:
        return
    
    flag = 0
    cleaning(nx, ny, d)

N, M = map(int, input().split())
r, c, d = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
flag = 1

cleaning(r, c, d)

cnt = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] == 1:
            cnt += 1

print(cnt)