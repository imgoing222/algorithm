# 16928 뱀과 사다리 게임
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque
import math

def bfs(cur_pos, cnt, end_point):
    Q = deque()
    Q.append([cur_pos, cnt])

    while Q:
        cur_pos, cnt = Q.popleft()

        for i in range(1, 7):
            next_pos = cur_pos + i
            
            if next_pos > end_point:
                break
            elif next_pos == end_point:
                return cnt+1

            if next_pos in ladders:
                Q.append([up[ladders.index(next_pos)], cnt+1])
            elif next_pos in snakes:
                pass
            else:
                Q.append([next_pos, cnt+1])

        
N, M = map(int, input().split())
ladders = []
up = []
snakes = []
min_ans = math.inf

for _ in range(N):
    x, y = map(int, input().split())
    ladders.append(x)
    up.append(y)

for _ in range(M):
    u, v = map(int, input().split())
    snakes.append(u)

for i in range(N):
    res = bfs(1, 0, ladders[i])
    ans = bfs(up[i], res, 100)
    print(ans)

    min_ans = min(ans, min_ans)

print(min_ans)