# 14500 테트로미노
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def dfs(x, y, cnt, total):
    global max_v

    if cnt == 3:
        max_v = max(max_v, total)
        return

    dx = (0, 1, 0)
    dy = (1, 0, -1)
    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue

        if not visited[nx][ny]:
            visited[nx][ny] = 1
            dfs(nx, ny, cnt+1, total+board[nx][ny])
            visited[nx][ny] = 0

def pink(x, y):
    global max_v

    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)
    for i in range(4):
        total = board[x][y]
        for j in range(i, i+3):
            nx = x + dx[j%4]
            ny = y + dy[j%4]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                break

            total += board[nx][ny]

        max_v = max(max_v, total)


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
max_v = 0

for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, 0, board[i][j])
        pink(i, j)
        visited[i][j] = 0

print(max_v)