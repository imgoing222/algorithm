import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def is_in_dots(a, b, c, d):
    global flag
    # 변에 있는 좌표를 보면서 dots에 있나 확인하기
    cnt = 0
    for i in range(d, c + 1):
        if (a, i) in dots:
            cnt += 1
        if (b, i) in dots:
            cnt += 1

    for j in range(a + 1, b):
        if (j, d) in dots:
            cnt += 1
        if (j, c) in dots:
            cnt += 1

    if cnt == N:
        flag += 1       

N = int(input())
dots = []

for _ in range(N):
    x, y = map(int, input().split())
    dots.append((x, y))

# x, y의 최소 최대값 찾기
i = sorted(dots)
j = sorted(dots, key=lambda x: x[1])
min_x = i[0][0]
max_x = i[N-1][0]
min_y = j[0][1]
max_y = j[N-1][1]

# x가 클때 y가 클때 범위 나눠서 정사각형 2번 만들기!!! (중요!!!)
flag = 0
if max_x - min_x > max_y - min_y:
    M = max_x - min_x
    is_in_dots(min_x, max_x, max_y, max_y - M)
    is_in_dots(min_x, max_x, min_y + M, min_y)
elif max_x - min_x < max_y - min_y:
    M = max_y - min_y
    is_in_dots(min_x, min_x + M, max_y, min_y)
    is_in_dots(max_x - M, max_x, max_y, min_y)
else:
    M = max_x - min_x
    is_in_dots(min_x, max_x, max_y, min_y)

# 변의 길이 print
if flag:
    print(M)
else:
    print(-1)


