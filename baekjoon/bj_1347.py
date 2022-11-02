# 1347 미로 만들기
import sys
sys.stdin = open('input.txt')


def maze(d):
    global x, y
    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)

    x = x + dx[d]
    y = y + dy[d]
    board[x][y] = '.'
   

N = int(input())
path = input()
board = [['#']*101 for _ in range(101)]

# 초기값
x = y = 50
board[x][y] = '.'
d = 2

for letter in path:
    # d 보정
    if d < 0:
        d += 4
    elif d > 3:
        d -= 4

    # 단어에 따라 움직이거나 방향전환
    if letter == 'F':
        maze(d)
    elif letter == 'R':
        d += 1
    elif letter == 'L':
        d -= 1

# 직사각형 만들기
x_li = []
y_li = []
for i in range(101):
    for j in range(101):
        if board[i][j] == '.':
            x_li.append(i)
            y_li.append(j)

# 프린트
for i in range(min(x_li), max(x_li)+1):
    for j in range(min(y_li), max(y_li)+1):
        print(board[i][j], end='')
    print()
