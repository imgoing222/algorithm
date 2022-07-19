import sys
sys.stdin = open('input.txt')
from itertools import combinations
from math import factorial

N = int(input())
n = N
r = 2
ans = 1

# NC2 * (N-2)C2 * ... * 2C2 구현 (전체중에 2개 뽑기 * 전체-2중에 2개 뽑기 * 전체-2-2중에 2개 뽑기 * ... * 2개중에 2개 뽑기)
while n != r:
    ans *= n * (n-1) // r
    n -= 2

# 뽑은 묶음이 순서와 상관 없으므로 (N/2)! 으로 중복 제거
ans //= factorial(N // r)

print(ans % (10**9+7))

