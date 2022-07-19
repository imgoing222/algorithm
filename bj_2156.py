# 2156 포도주 시식
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
if n == 1:
    print(int(input()))
    exit()
else:
    wines = []
    for i in range(n):
        wines.append(int(input()))

    dp = [0]*n
    dp[0] = wines[0]
    dp[1] = wines[0] + wines[1]

    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2]+wines[i], dp[i-3]+wines[i-1]+wines[i])

    print(dp[-1])
