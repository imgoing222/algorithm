# 3190 뱀
# deque 쓰면 훨ㄹㄹㄹㄹㄹㄹㄹ씬 쉬움
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)
def go_snake(x, y, d):
    cnt = tail = 1

    while True:
        nx = x + dx[d]
        ny = y + dy[d]

        if nx < 0 or ny < 0 or nx >= N or ny >= N or (board[nx][ny] != -1 and board[nx][ny] != 0):
            print(cnt)
            return

        if board[nx][ny] == 0:
            board[nx][ny] = board[x][y] + 1
            # 여기가 시간 오래 걸리는 이유인듯...?
            for i in range(N):
                for j in range(N):
                    if board[i][j] == tail:
                        board[i][j] = 0
                        break
            tail += 1
        else:
            board[nx][ny] = board[x][y] + 1

        if dir[cnt] == 'L':
            d = (d-1)%4
        elif dir[cnt] == 'D':
            d = (d+1)%4

        x = nx
        y = ny
        cnt += 1

        
N = int(input())
board = [[0]*N for _ in range(N)]

K = int(input())
for _ in range(K):
    x, y = map(int, input().split())
    board[x-1][y-1] = -1

L = int(input())
dir = [0]*10001
for _ in range(L):
    X, C = input().split()
    dir[int(X)] = C

board[0][0] = 1
go_snake(0, 0, 0)