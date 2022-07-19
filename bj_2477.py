import sys
sys.stdin = open('input.txt')

K = int(input())

d_li = []
a_li = []

## 돌면서 d_li과 a_li 각각 나눠 받기
for _ in range(6):
    d, a = map(int, input().split())
    d_li.append(d)
    a_li.append(a)

# 전체 큰 직사각형
rectangular = 1

# 3131/4242/2323/1414 경우로 나누어서 계산
case = [(1, 3), (2, 4), (3, 2), (4, 1)]

for x, y in case:
    if d_li.count(x) == 2 and d_li.count(y) == 2:
        flag = 0
        while True:
            #  받은 순서 pop하고 뒤로 보내서 맞춰주기
            if d_li[0] == x or d_li[0] == y:
                k = d_li.pop(0)
                d_li.append(k)
                h = a_li.pop(0)
                a_li.append(h)
            else:
                flag += 1
                d_li.pop(0)
                rectangular *= a_li.pop(0)

            if flag == 2:
                break

# a_li에 작은 직사각형 그리는 순서대로 정렬시켰으므로 idx 1,2번이 작은 직사각형의 가로와 세로

print(K * (rectangular-a_li[1]*a_li[2]))




