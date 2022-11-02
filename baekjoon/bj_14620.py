# 14620 꽃길
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)
def flower(cnt, cost):
    global min_cost

    # 세번째 꽃
    if cnt == 3:
        print(visited, cost, min_cost)
        min_cost = min(min_cost, cost)
        return

    for i in range(N):
        for j in range(N):
            if 0 <= i-1 < N and 0 <= i+1 < N and 0 <= j-1 < N and 0 <= j+1 < N:
                if not visited[i][j] and not visited[i-1][j] and not visited[i+1][j] and not visited[i][j-1] and not visited[i][j+1]:
                    
                    # 꽃술 그리기
                    visited[i][j] = 1
                    # 꽃잎 그리기
                    for d in range(4):
                        visited[i+dx[d]][j+dy[d]] = 1

                    flower(cnt+1, cost + garden[i][j] + garden[i-1][j] + garden[i+1][j] + garden[i][j+1] + garden[i][j-1])

                    visited[i][j] = 0
                    for d in range(4):
                        visited[i+dx[d]][j+dy[d]] = 0

    
N = int(input())
garden = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
min_cost = 200*100

flower(0, 0)

print(min_cost)