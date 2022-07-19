# 16173 점프왕 쩰리 (Small)
import sys
sys.stdin = open('input.txt')

def jump(x, y):
    range = board[x][y]
    if range == -1:
        print('HaruHaru')
        exit()
    elif range == 0:
        return

    for dx, dy in (0, 1), (1, 0):
        if 0 <= x + dx*range < N and 0 <= y + dy*range < N:
            jump(x + dx*range, y + dy*range)
        
    
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

jump(0, 0)
print('Hing')