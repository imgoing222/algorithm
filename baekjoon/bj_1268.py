n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

# board row, column swap
new_board = list(map(list, zip(*board)))

# 1번 학생부터 1학년 ~ 5학년 비교해서 count 후 set에 넣어서 중복 제거 후 길이를 res에 append ... (반복)
res = []
for i in range(n):
    cnt = set()
    for j in range(len(new_board)):
        for k in range(n):
            if new_board[j][i] == new_board[j][k] and i != k:
                cnt.add(k)
    res.append(len(cnt))

leader = 0
for x in range(len(res)):
    if res[x] > res[leader]:
        leader = x

print(leader + 1)






