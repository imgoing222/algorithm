import sys
sys.stdin = open('input.txt')

# for문 돌면서 만족하는 계수 중 가장 작은 것!!!
def solve():
    for i in range(1, 11):
        for j in range(1, 11):
            for k in range(1, 11):
                if i*c1 + j*c2 == k*c3 and i*h1 + j*h2 == k*h3 and i*o1 + j*o2 == k*o3:
                    print(i, j, k)
                    return

# C, H, O 카운트
def cnt(m):
    c = m.count('C')
    h = m.count('H')
    o = m.count('O') 
    
    for x in range(len(m)):
        if m[x] in ['2','3','4','5','6','7','8','9']:
            if m[x-1] == 'C':
                c += int(m[x]) - 1
            elif m[x-1] == 'H':
                h += int(m[x]) - 1
            else:
                o += int(m[x]) - 1 

    return c, h, o

# M1, M2, M3 나누기... 이게 맞나....? 풀고나면 다른 코드 참고할 것
M1, M = input().split('+')
M2, M3 = M.split('=')

# 각각에 들어있는 c, h, o 카운트 함수로 세기 -> def cnt()
c1, h1, o1 = cnt(M1)
c2, h2, o2 = cnt(M2)
c3, h3, o3 = cnt(M3)

# 정답 구하기 -> def solve()
solve()

