# 8911 거북이
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def change_dir(order):
    global cur_d

    if order == 'L':
        cur_d = (cur_d - 1) % 4
    else:
        cur_d = (cur_d + 1) % 4


T = int(input())

for _ in range(T):
    orders = input()
    pos_x = pos_y = 0
    min_x = max_x = min_y = max_y =0
    cur_d = 0

    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)

    for order in orders:
        if order == 'F':
            pos_x += dx[cur_d]
            pos_y += dy[cur_d]
        elif order == 'B':
            pos_x -= dx[cur_d]
            pos_y -= dy[cur_d]
        else:
            change_dir(order)

        if pos_x < min_x: min_x = pos_x
        if pos_x > max_x: max_x = pos_x
        if pos_y < min_y: min_y = pos_y
        if pos_y > max_y: max_y = pos_y

    print((max_x - min_x) * (max_y - min_y))

