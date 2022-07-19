N, m, M, T, R = map(int, input().split())
X = m
n = i = 0

if m + T > M:
    print(-1)
else:
    while n != N:
        if X + T > M:
            if X - R < m:
                X = m
            else:
                X -= R
        else:
            n += 1
            X += T
        i += 1
    print(i)


