import sys
sys.stdin = open('input.txt')

S, C = map(int, input().split())

veggies = []
for _ in range(S):
    L = int(input())
    veggies.append(L)

shortest = min(veggies)
longest = max(veggies)

n = 0
max_length = 0

while True:
    if shortest * C < longest:
        max_length = longest // C
        break
    elif shortest * C >= longest:
        max_length = shortest - n
        temp = 0
        for length in veggies:
            temp += length // max_length
        if temp < C:
            n += 1
            continue
        break

print(sum(veggies) - max_length*C)