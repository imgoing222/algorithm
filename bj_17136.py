import sys
sys.stdin = open('input.txt')

# 5x5 -> 1x1 순서로 탐색
def paper(x, y, n):
    global ans, flag

    for i in range(n):
        for j in range(n):
            if x+i < 0 or x+i >= N or y+j < 0 or y+j >= N:
                return
            if board[x+i][y+j] == 0:
                return

    ans += 1
    cnt[n-1] -= 1
    if cnt[n-1] == 0:
        ans -= 1
        flag = 1
        return

    for i in range(n):
        for j in range(n):
            if 0 <= x+i < N and 0 <= y+j < N:   
                board[x+i][y+j] = 0
    

def solve(k):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                paper(i, j, k)
                if flag:
                    return


N = 10
board = [list(map(int, input().split())) for _ in range(N)]
cnt = [6, 6, 6, 6, 6]
ans = 0


k = 5
while k > 0:
    flag = 0
    solve(k)
    k -= 1


print(cnt)
if flag:
    print(-1)
else:
    print(ans)