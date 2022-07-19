# 20493 세상은 하나의 손수건
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, T = map(int, input().split())

d = ([1, 0], [0, -1], [-1, 0], [0, 1])
x = y = t1 = 0
cur_d = 0

# 방향 전환하는 경우
for _ in range(N):
    t2, dir = input().split()
    t2 = int(t2)
    
    x += d[cur_d][0] * (t2 - t1)
    y += d[cur_d][1] * (t2 - t1)

    # 방향 전환 (연주님 코드 줍줍 감사합니당)
    if dir == 'left':
        cur_d = (cur_d-1) % 4
    else:
        cur_d = (cur_d+1) % 4

    t1 = t2

# 남은 거리
x += d[cur_d][0] * (T-t1)
y += d[cur_d][1] * (T-t1)


print(x, y)
