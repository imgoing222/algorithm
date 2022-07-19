N, M = map(int, input().split())
r = {i for i in range(N)}
c = {i for i in range(M)}
li_rc = []

for i in range(N):
    li_rc.append(list(input()))

for i in range(N):
    for j in range(M):
        if li_rc[i][j] == 'X':
            r.discard(i)
            c.discard(j)

a = len(r)
b = len(c)

print((abs(a - b) + min(a, b)))
