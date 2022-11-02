import sys
sys.stdin = open('input.txt')

def rotate(N, d):
    # 극이 같은지 다른지 판단하기 위해서 초록색 점선 데려오기
    targets = []
    for i in range(1, T):
        targets += [Gears[i][2], Gears[i+1][6]]

    # 시계방향
    if d == 1:
        cw_turn(N)
    # 반시계방향
    elif d == -1:
        ccw_turn(N)

    # 기준으로부터 왼쪽
    flag = d
    for j in range(2*(N-1)-1, 0, -2):
        if targets[j] == targets[j-1]:
            break
        else:
            if flag == 1:
                ccw_turn((j+1)//2)
                flag = -1
            elif flag == -1:
                cw_turn((j+1)//2)
                flag = 1
            
    # 기준으로부터 오른쪽
    flag = d
    for j in range(2*(N-1), 2*(T-2)+1, 2):
        if targets[j] == targets[j+1]:
            break
        else:
            if flag == 1:
                ccw_turn(j//2+2)
                flag = -1
            elif flag == -1:
                cw_turn(j//2+2)
                flag = 1


# 시계방향으로 회전 함수
def cw_turn(n):
    tmp = Gears[n].pop()
    Gears[n].insert(0, tmp)

# 반시계방향으로 회전 함수
def ccw_turn(n):
    tmp = Gears[n].pop(0)
    Gears[n].append(tmp)


T = int(input())
Gears = [[0]] + [list(map(int, input())) for _ in range(T)]
K = int(input())

for _ in range(K):
    N, d = map(int, input().split())
    rotate(N, d)

ans = 0
for i in range(1, T+1):
    if Gears[i][0] == 1:
        ans += 1

print(ans)