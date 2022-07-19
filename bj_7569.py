# 7569 토마토
import sys
sys.stdin = open('input.txt')
from collections import deque

# 토마토 탐색
def bfs():
    Q = deque()
    cnt = 0
    
    # 처음 토마토 위치, 카운트 횟수 Q에 다 담기
    for z in range(1, H+1):
        for x in range(N*(z-1), N*z):
            for y in range(M):
                if tomato[x][y] == 1:
                    Q.append([x, y, z, cnt])
    
    while Q:
        # 토마토 큐에서 꺼내서 익혀주기
        x, y, z, cnt = Q.popleft()
        tomato[x][y] = 1
        # 덜 익었다면
        if not delicious():
            # 앞뒤좌우 토마토
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < N*(z-1) or nx >= N*z or ny < 0 or ny >= M:
                    continue
                
                if tomato[nx][ny] == 0 and not visited[nx][ny]:
                    Q.append([nx, ny, z, cnt+1])
                    visited[nx][ny] = 1

            # 위아래 토마토
            for j in range(-1, 2):
                nz = z + j

                if nz < 1 or nz > H:
                    continue
                
                if tomato[x+N*j][y] == 0 and not visited[x+N*j][y]:
                    Q.append([x+N*j, y, nz, cnt+1])
                    visited[x+N*j][y] = 1

            
        # 다 익었다면 카운트 횟수 반환
        else:
            return cnt

    # 토마토 다 탐색해도 덜 익었다면 -1 반환
    return -1


# 토마토 다 익었는지 확인
def delicious():
    for i in range(N*H):
        for j in range(M):
            if tomato[i][j] == 0:
                return
    return 1


M, N, H = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N*H)]
visited = [[0]*M for _ in range(N*H)]

# 앞뒤좌우
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)


# 탐색 시작
print(bfs())