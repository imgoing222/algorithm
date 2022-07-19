# 1149 RGB 거리

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*3 for _ in range(N)]

# 1번 집 초기화
for i in range(3):
    dp[0][i] = cost[0][i]

for i in range(1, N):
    for j in range(3):
        dp[i][j] = cost[i][j] + min(dp[i-1][(j+1)%3], dp[i-1][(j+2)%3])

print(min(dp[N-1]))

