import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def omok(x, y, n):
    dx = (-1, 0, 1, 1)
    dy = (1, 1, 1, 0)

    for i in range(4):
        cnt = 1
        for k in range(1, 5):
            if 1 <= x + dx[i]*k < 20 and 1 <= y + dy[i]*k < 20 and board[x + dx[i]*k][y + dy[i]*k] == n:
                cnt += 1
        if cnt == 5:
            # 6목 판정
            if board[x + dx[i]*5][y + dy[i]*5] == n or board[x + dx[i]*(-1)][y + dy[i]*(-1)] == n:
                return 0
            else:
                return 1
    return 0

board = [[0]*21] + [[0] + list(map(int, input().split())) + [0] for _ in range(19)] + [[0]*21]

for i in range(1, 20):
    for j in range(1, 20):
        if board[i][j]:
            if omok(i, j, board[i][j]):
                print(board[i][j])
                print(i, j)
                exit()

print(0)
