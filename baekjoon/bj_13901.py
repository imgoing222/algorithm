# 13901 로봇
import sys
sys.stdin = open('input.txt')


def move(x, y):
    
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    d = 0
    flag = 0
    while True:
        # 2로 방문체크
        room[x][y] = 2

        nx = x + dx[dir[d % 4]-1]
        ny = y + dy[dir[d % 4]-1]

        # 4방향 모두 실패했을 때
        if flag == 4:
            print(x, y)
            break
        
        # 벽
        if nx < 0 or ny < 0 or nx >= R or ny >= C:
            flag += 1
            d += 1
            continue
        
        # 방문 또는 장애물
        if room[nx][ny]:
            flag += 1
            d += 1
            continue
        
        x = nx
        y = ny
        flag = 0
        

R, C = map(int, input().split())
room = [[0]*C for _ in range(R)]

# 장애물 받아서 room에 1로 넣어주기
k = int(input())
for _ in range(k):
    br, bc = map(int, input().split())
    room[br][bc] = 1

sr, sc = map(int, input().split())

dir = list(map(int, input().split()))

move(sr, sc)

