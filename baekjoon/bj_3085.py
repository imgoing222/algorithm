import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def longest_candy():
    
    global ans

    for i in range(N):
        tmp = 1
        for j in range(N-1):
            if board[i][j] == board[i][j+1]:
                tmp += 1
            else:
                if tmp > ans:
                    ans = tmp
                tmp = 1
        if tmp > ans:
            ans = tmp
            

    for j in range(N):
        tmp = 1
        for i in range(N-1):
            if board[i][j] == board[i+1][j]:
                tmp += 1
            else:
                if tmp > ans:
                    ans = tmp
                tmp = 1
        if tmp > ans:
            ans = tmp
        

N = int(input())
board = [list(input().rstrip()) for _ in range(N)]
ans = 0

# 색이 다른 인접한 두칸 고르기
# 1) 행 기준
for i in range(N):
    for j in range(N-1):
        if board[i][j] != board[i][j+1]:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            longest_candy()
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]


# 2) 열 기준
for j in range(N):
    for i in range(N-1):
        if board[i][j] != board[i+1][j]:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            longest_candy()
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

print(ans)