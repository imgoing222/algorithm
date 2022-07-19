# 11559 Puyo Puyo
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

    
# 뿌요 4개 이상인지 체크
def puyo_enough(x, y, c):
    Q = deque()
    Q.append([x, y])
    cnt = 0
    x1 = x
    y1 = y

    while Q:
        x, y = Q.popleft()
        visited[x][y] = 1
        cnt += 1

        if cnt == 4:
            # 처음 x, y로 뿌요 터뜨리기
            puyo_boom(x1, y1, c)
            return 1

        dx = (-1, 0, 1, 0)
        dy = (0, 1, 0, -1)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= 12 or ny >= 6:
                continue

            if visited[nx][ny]:
                continue
            
            if field[nx][ny] == c:
                Q.append([nx, ny])
                visited[nx][ny] = 1
    
    return 0

# 뿌요 터트리기
def puyo_boom(x, y, c):
    Q = deque()
    Q.append([x, y])
    
    while Q:
        x, y = Q.popleft()
        field[x][y] = '.'

        dx = (-1, 0, 1, 0)
        dy = (0, 1, 0, -1)
        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= 12 or ny >= 6:
                continue
            
            if field[nx][ny] == c:
                Q.append([nx, ny])



# 남은 공간으로 뿌요 내리기
def puyo_down():
    while True:
        flag = 1
        for i in range(11, 0, -1):
            for j in range(6):
                if field[i][j] == '.':
                    if field[i-1][j] in puyo_color:
                        field[i][j], field[i-1][j] = field[i-1][j], field[i][j]
                        flag = 0

        if flag:
            return


field = [list(input().rstrip()) for _ in range(12)]
puyo_color = ['R', 'G', 'B', 'P', 'Y']

cnt = 0
# 뿌요 찾고 터뜨리고 내리기
while True:
    ret = 0
    for i in range(12):
        for j in range(6):
            visited = [[0]*6 for _ in range(12)]
            for color in puyo_color:
                if field[i][j] == color:
                    ret += puyo_enough(i, j, color)
                    
    cnt += 1
    if ret == 0:
        print(cnt-1)
        break
    else:
        puyo_down()



        
