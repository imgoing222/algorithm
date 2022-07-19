import sys
sys.stdin = open('input.txt')

def bfs(y, x):
    global cnt
    Q = []

    # 방문했던 곳이면 바로 return
    if ground[y][x] == 9:
        return 0

    # enQ
    Q.append([y, x])
    ground[y][x] = 9

    while Q:
        y, x = Q.pop(0)
        flag = 1
        # 인접중에 1인 곳 and 벽 아닌 곳
        dy = (1, 0, -1, 0)
        dx = (0, 1, 0, -1)
        for i in range(4):
            # 네 방향 움직이면서 갈 수 있는 곳 모두 append 후 visited로 변경
            if 0 <= x + dx[i] < M and 0 <= y + dy[i] < N and ground[y + dy[i]][x + dx[i]] == 1:
                Q.append([y + dy[i], x + dx[i]])
                ground[y + dy[i]][x + dx[i]] = 9

    return 1

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    ground = [[0] * M for _ in range(N)]
    veggie = [list(map(int, input().split())) for _ in range(K)]
    cnt = 0

    # 배추밭 만들기
    for i in range(K):
        x, y = veggie[i][0], veggie[i][1]
        ground[y][x] = 1

    # K번 bfs 돌리기
    for j in veggie:
        cnt += bfs(j[1], j[0])

    print(cnt)