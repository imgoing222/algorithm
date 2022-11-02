# 16924 십자가 찾기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 십자가 판별
def isCross(x, y):

    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)
    t = 1
    while True:
        for i in range(4):
            nx = x + dx[i] * t
            ny = y + dy[i] * t

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                return x, y, t-1

            if board[nx][ny] == '.':
                return x, y, t-1

        # 4방향 모두 통과하면 visited 체크
        for i in range(4):
            nx = x + dx[i] * t
            ny = y + dy[i] * t
            
            board[x][y] = 1
            board[nx][ny] = 1
        
        t += 1



N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
k = 0
ans = []

# 별 찾기
for i in range(N):
    for j in range(M):
        if board[i][j] == '*' or board[i][j] == 1:
            x, y, s = isCross(i, j)
            if s:
                ans.append([x+1, y+1, s])
                k += 1

# 별이 남았으면 실패
for i in range(N):
    for j in range(M):
        if board[i][j] == '*':
            print(-1)
            exit()

print(k)
for cross in ans:
    print(*cross)