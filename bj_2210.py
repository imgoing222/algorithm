# 2210 숫자판 점프
import sys
sys.stdin = open('input.txt')

def make_number(x, y, cnt, num):
    if cnt == 5:
        ans.add(num)
        return

    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= 5 or ny >= 5:
            continue

        make_number(nx, ny, cnt+1, num + board[nx][ny])


board = [list(input().split()) for _ in range(5)]
ans = set()

for i in range(5):
    for j in range(5):
        make_number(i, j, 0, board[i][j])

print(len(ans))