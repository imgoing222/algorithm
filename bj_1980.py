import sys
sys.stdin = open('input.txt')

n, m, T = map(int, input().split())

max_b = 0
min_c = 987654321
i = 0

while i < T + 1:
    t = T
    burger = coke = 0
    burger += (t - i) // m
    coke += (t - i) % m
    burger += i // n
    coke += i % n
    i += 1

    if n > m:
        if min_c > coke:
            min_c = coke
            max_b = burger
    else:
        if min_c >= coke:
            min_c = coke
            max_b = burger

print(max_b, min_c)