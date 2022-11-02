import sys
sys.stdin = open('input.txt')

def move(d):
    global kx, ky, sx, sy

    nkx = kx + dir[d][0]
    nky = ky + dir[d][1]

    # 킹이 체스판을 벗어나면 return
    if nkx < 1 or nkx > 8 or nky < 1 or nky > 8: 
        return

    # 킹과 돌의 위치가 같을 경우
    if nkx == sx and nky == sy:
        #  같은 방향으로 옮기기
        nsx = sx + dir[d][0]
        nsy = sy + dir[d][1]

        # 옮긴 돌의 위치가 체스판을 벗어나면 return 
        if nsx < 1 or nsx > 8 or nsy < 1 or nsy > 8: 
            return

        sx = nsx
        sy = nsy
 
    kx = nkx
    ky = nky


board = [[0]*9 for _ in range(9)] 
king, stone, N = input().split()

# 킹과 돌의 위치
kx = ord(king[0]) - 64
ky = int(king[1])
sx = ord(stone[0]) - 64
sy = int(stone[1])

dir = {
    'R' : [1, 0],
    'L' : [-1, 0],
    'B' : [0, -1],
    'T' : [0, 1],
    'RT' : [1, 1],
    'LT' : [-1, 1],
    'RB' : [1, -1],
    'LB' : [-1, -1],
}

for _ in range(int(N)):
    d = input()
    move(d)

print(chr(kx+64)+str(ky))
print(chr(sx+64)+str(sy))