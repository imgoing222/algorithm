# 15787 기차가 어둠을 헤치고
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def order_1(i, x):
    trains[i-1][x-1] = 1

def order_2(i, x):
    trains[i-1][x-1] = 0

def order_3(i):
    trains[i-1][19] = 0
    for j in range(18, -1, -1):
        if trains[i-1][j] == 1:
            trains[i-1][j+1] = 1
            trains[i-1][j] = 0

def order_4(i):
    trains[i-1][0] = 0
    for j in range(1, 20):
        if trains[i-1][j] == 1:
            trains[i-1][j-1] = 1
            trains[i-1][j] = 0


N, M = map(int, input().split())

# 초기 기차
trains = [[0]*20 for _ in range(N)]

# 명령 실행 
for m in range(M):
    order = list(map(int, input().split()))

    if order[0] == 1:
        order_1(order[1], order[2])
    elif order[0] == 2:
        order_2(order[1], order[2])
    elif order[0] == 3:
        order_3(order[1])
    elif order[0] == 4:
        order_4(order[1])

# 중복 기차 제거
ans = []
for train in trains:
    if train not in ans:
        ans.append(train)

print(len(ans))