import sys
sys.stdin = open('input.txt')

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

def signal(x, y, d):
    global time, voyager, idx
    d1 = d
     
    while True:
        nx = x + dx[d]
        ny = y + dy[d]

        # 무한히 반복되는 경우
        if nx == PR-1 and ny == PC-1 and d == d1:
            voyager = 1
            return

        # 항성계 벗어난 경우
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            break

        # 블랙홀 만난 경우
        elif board[nx][ny] == 'C':
            break
        
        # / 만난 경우
        elif board[nx][ny] == '/':
            if d % 2:
                d -= 1
            else:
                d += 1

        # \ 만난 경우
        elif board[nx][ny] == '\\':
            d = 3 - d

        x = nx
        y = ny
        time += 1



    
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
PR, PC = map(int, input().split())
voyager = 0

dir = { 0: 'U', 1: 'R', 2: 'D', 3: 'L'}

idx = max_time = 0
for d in range(4):
    time = 1
    signal(PR-1, PC-1, d)
    if max_time < time:
        max_time = time
        idx = d

# 방향과 걸린 시간 출력



