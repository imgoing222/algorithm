N = int(input())
numbers = list(map(int, input().split()))

max_v = numbers[0]
min_v = numbers[0]

for i in range(N):
    if numbers[i] > max_v:
        max_v = numbers[i]
    if numbers[i] < min_v:
        min_v = numbers[i]

print(f'{min_v} {max_v}')