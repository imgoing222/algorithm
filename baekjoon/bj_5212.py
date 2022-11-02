# 5212 지구 온난화
import sys
sys.stdin = open('input.txt')
    
def global_warming(x, y):
    global cnt

    # 4방향 탐색하면서 잠길땅인지 아닌지 살펴보기
    dx = (1, -1, 0, 0)
    dy = (0, 0, -1, 1)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if map_of_2071[nx][ny] == '.':
            cnt += 1
        
        if cnt == 3:
            underwater.append([x, y])
            return


def small_map():
    for i in range(R+2):
        for j in range(C+2):
            if map_of_2071[i][j] == 'X':
                x_li.append(i)
                y_li.append(j)


R, C = map(int, input().split())
map_of_2071 = [['.']*(C+2)] + [['.'] + list(input()) + ['.'] for _ in range(R)] + [['.']*(C+2)]
underwater = []

# 땅이라면 global warming 함수로 이동
for i in range(1, R+1):
    for j in range(1, C+1):
        if map_of_2071[i][j] == 'X':
            cnt = 0
            global_warming(i, j)


# 잠길 땅들 지도에서 바다로 바꿔주기
for coord in underwater:
    map_of_2071[coord[0]][coord[1]] = '.'


# 가장 작은 크기의 지도 만들기
x_li = []
y_li = []
small_map()

for i in range(min(x_li), max(x_li)+1):
    print(''.join(map_of_2071[i][min(y_li):max(y_li)+1]))