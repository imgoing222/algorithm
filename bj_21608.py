#21608 상어 초등학교
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)
def chk1():
    max_v = -1
    best_seat = []

    for i in range(N):
        for j in range(N):
            if shark_class[i][j] == 0:
                cnt = 0
                for k in range(4):
                    if 0 <= i + dx[k] < N and 0 <= j + dy[k] < N:
                        if shark_class[i+dx[k]][j+dy[k]] in likes:
                            cnt += 1

                if max_v <= cnt:
                    if max_v < cnt:
                        best_seat = []
                    max_v = cnt
                    best_seat.append([i, j])

    if len(best_seat) == 1:
        return best_seat[0]
    else:
        return chk2(best_seat)

def chk2(arr):
    max_v = -1
    best_seat = []

    for seat in arr:
        x = seat[0]
        y = seat[1]
        cnt = 0
        for k in range(4):
            if 0 <= x + dx[k] < N and 0 <= y + dy[k] < N:
                if shark_class[x+dx[k]][y+dy[k]] == 0:
                    cnt += 1
        
        if max_v <= cnt:
            if max_v < cnt:
                best_seat = []
            max_v = cnt
            best_seat.append(seat)

    if len(best_seat) == 1:
        return best_seat[0]
    else:
        return chk3(best_seat)

def chk3(arr):
    return sorted(arr, key = lambda x: (x[0], x[1]))[0]


N = int(input())
shark_class = [[0]*N for _ in range(N)]
students_and_likes = {}

for _ in range(N*N):
    arr = list(map(int, input().split()))
    student = arr[0]
    likes = arr[1:]
    students_and_likes[student] = likes

    x, y = chk1()
    shark_class[x][y] = student

satisfaction = [0, 1, 10, 100, 1000]
ans = 0
for i in range(N):
    for j in range(N):
        cnt = 0
        for k in range(4):
            if 0 <= i + dx[k] < N and 0 <= j + dy[k] < N:
                if shark_class[i+dx[k]][j+dy[k]] in students_and_likes[shark_class[i][j]]:
                    cnt += 1

        ans += satisfaction[cnt]

print(ans)
                