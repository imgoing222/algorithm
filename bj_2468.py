# 2468 안전영역
import sys
sys.setrecursionlimit(10000)
from itertools import chain
sys.stdin = open('input.txt')

def find_safezone(x, y):
    visited[x][y] = 1

    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
    
        if underwater[nx][ny] and not visited[nx][ny]:
            find_safezone(nx, ny)


N = int(input())
region = [list(map(int, input().split())) for _ in range(N)]
# 2차원 리스트를 1차원 리스트로 변환하고, set으로 중복제거하여 맵 안의 높이 중 가장 높은 값 찾기
max_h = max(set(chain(*region)))
ans = []

# 비가 0만큼 올때 ~ 맵 안의 가장 높은 값만큼 올때
for k in range(max_h + 1):
    visited = [[0]*N for _ in range(N)]
    underwater = [[1]*N for _ in range(N)]
    # k만큼의 비가 내릴 때 잠기는 영역 underwater에 표시해주기
    # 잠기는 영역: 0 , 안 잠기는 영역: 1
    for i in range(N):
        for j in range(N):
            if region[i][j] <= k:
                underwater[i][j] = 0
    
    # 안전영역 찾기
    cnt = 0
    for i in range(N):
        for j in range(N):
            if underwater[i][j] and not visited[i][j]:
                find_safezone(i, j)
                cnt += 1
    
    ans.append(cnt)

print(max(ans))
