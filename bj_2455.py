max_v = 0
total = 0

for _ in range(4):  
    o, i = map(int, input().split())
    total -= o
    if total > max_v:
        max_v = total
    total += i
    if total > max_v:
        max_v = total

print(max_v)

