import sys
#sys.stdin = open('input.txt')
input = sys.stdin.readline

def locate_piece(num, coordinates, piece_name):
    for i in range(0, num):
        board[coordinates[i*2]-1][coordinates[i*2+1]-1] = piece_name

def check_queen(x, y):
    dx = (-1, -1, 0, 1, 1, 1, 0, -1)
    dy = (0, 1, 1, 1, 0, -1, -1, -1)

    for i in range(8):
        step = 1
        while True:
            nx = x + dx[i] * step
            ny = y + dy[i] * step

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                break

            if board[nx][ny] in piece:
                break

            board[nx][ny] = 1
            step += 1

def check_knight(x, y):
    dx = (-2, -2, -1, -1, 1, 1, 2, 2)
    dy = (-1, 1, 2, -2, 2, -2, 1, -1)

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        
        if board[nx][ny] in piece:
            continue

        board[nx][ny] = 1

n, m = map(int, input().split())
# board = [[0] * m] * n
# 이렇게 짜면 [0] * m 을 n개 만큼 복사하는 거라서 가리키는 주소가 같다 (얕은 복사)
# 2차원 리스트 짤 때 주의할 것!!!!
board = [[0] * m for _ in range(n)]
piece = ["Q", "K", "P"]

for i in range(3):
    piece_info = list(map(int, input().split()))
    locate_piece(piece_info[0], piece_info[1:], piece[i])

for i in range(n):
    for j in range(m):
        if board[i][j] == "Q":
            check_queen(i, j)
        elif board[i][j] == "K":
            check_knight(i, j)
                       
ans = 0
for row in board:
    ans += row.count(0) 

print(ans)