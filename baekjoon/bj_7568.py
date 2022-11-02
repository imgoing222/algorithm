import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
data = [tuple(map(int, input().split())) for _ in range(N)]

for i in data:
    cnt = 1
    for j in range(N):
        if i[0] < data[j][0] and i[1] < data[j][1]:
            cnt += 1
    print(cnt, end=' ')