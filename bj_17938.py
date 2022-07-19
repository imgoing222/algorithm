# 17938 퐁당퐁당 2
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
P, T = map(int, input().split())

arr = ( [i for i in range(1, 2*N+1)] + [i for i in range(2*N-1, 1, -1)] ) * 10000

total_arms = 0
num_of_arms = 0
for i in range(T):
    total_arms += arr[i]
    num_of_arms = arr[i]

range_of_arms = range(total_arms - num_of_arms + 1, total_arms + 1)
for i in range_of_arms:
    if i % (2*N) == (2*P-1) or i % (2*N) == (2*P):
        print('Dehet YeonJwaJe ^~^')
        break
else:
    print('Hing...NoJam')