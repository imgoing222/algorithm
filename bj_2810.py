n = int(input())

seat = input()
res = n + 1 - (seat.count('L') * 0.5)

if res > n:
    print(n)
else:
    print(int(res))