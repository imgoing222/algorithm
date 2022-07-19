# 10844 쉬운 계단 수
import sys
sys.stdin = open('input.txt')

def isStair(x, depth):
    global cnt
    if depth == N:
        memo[N] = memo[N-1] + cnt
        last_number[N].append(x)
        return
    
    else:
        if 0 <= x-1 <= 9:
            cnt = (cnt + 1) % 1000000000
            isStair(x-1, depth+1)
        if 0 <= x+1 <= 9:
            cnt = (cnt + 1) % 1000000000
            isStair(x+1, depth+1)

N = int(input())
cnt = 0
memo = [0]*N
last_number = [[] for _ in range(N)]

for i in range(1, N+1):
    isStair(i, 10)

print(cnt)