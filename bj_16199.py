y, m, d = map(int, input().split())
y1, m1, d1 = map(int, input().split())

# 만 나이
if m1 < m:
    print(y1 - y - 1)
elif m1 == m:
    if d1 >= d:
        print(y1 - y)
    else:
        print(y1 - y - 1)
else:
    print(y1 - y)

# 세는 나이
print(y1 - y + 1)

# 연 나이
print(y1 - y)