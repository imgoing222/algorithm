import sys
sys.stdin = open('input.txt')

board = [list(input()) for _ in range(8)]
ans = 0

for i in range(8):
    for j in range(8):
        if board[i][j] == 'F' and (i + j) % 2 == 0:
            ans += 1

print(ans)