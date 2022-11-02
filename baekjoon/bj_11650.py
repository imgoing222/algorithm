import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
numbers = [list(map(int, input().split())) for _ in range(N)]

new_numbers = sorted(numbers, key = lambda x : [x[0], x[1]])

for i in range(N):
    print(*(new_numbers[i]))