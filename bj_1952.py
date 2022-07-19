M, N = map(int, input().split())

board = [[0]*N for _ in range(M)]

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
a, b = 0, -1

i = 0
cnt = 0
res = 0

while cnt != M*N:
    tmpa = a + d[i][0]
    tmpb = b + d[i][1]

    if 0 <= tmpa < M and 0 <= tmpb < N and board[tmpa][tmpb] == 0:
        a, b = tmpa, tmpb
        cnt += 1
        board[a][b] = cnt
    else:
        i = (i + 1) % 4
        res += 1

print(res)