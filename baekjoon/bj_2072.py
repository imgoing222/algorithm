import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def omok(p):
    for x in range(19):
        for y in range(19):
            if board[x][y] == p:
            
                dx = (-1, -1, -1, 0, 1, 1, 1, 0)
                dy = (-1, 0, 1, 1, 1, 0, -1, -1)

                for d in range(8):
                    cnt = 1
                    for n in range(1, 5):
                        tmpx = x + dx[d]*n
                        tmpy = y + dy[d]*n
                        if 0 <= tmpx < 19 and 0 <= tmpy < 19 and board[tmpx][tmpy] == p:
                            cnt += 1
                    
                    if cnt == 5:
                        # 6목은 안돼!!!!!!
                        if 0 <= x + dx[d]*5 < 19 and 0 <= y + dy[d]*5 < 19 and board[x + dx[d]*5][y + dy[d]*5] == p:
                            return 0
                        else:
                            return 1

    return 0


N = int(input())
board = [[0]*19 for _ in range(19)]

for i in range(1, N + 1):
# 흑돌 1, 백돌 2
    x, y = map(int, input().split())
    if i % 2:
        board[x-1][y-1] = 1
    else:
        board[x-1][y-1] = 2
    
    if omok(board[x-1][y-1]):
        print(i)
        exit()

print(-1)