# 3019 테트리스
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def when_block_is_down(arr):
    global cnt

    # 현재 필드
    field = [[0]*C for _ in range(R)]
    for i in range(C):
        for j in range(floor[i]):
            field[j][i] = 1

    i = 0
    while True:
        valid = 0
        for c, r in arr:
            if field[r + i][c] == 0:
                valid += 1
        if valid == 4:
            max_h = i
            break
        else:
            i += 1
            

    for c, r in arr:
        field[r + max_h][c] = 1

    for i in range(R):
        for j in range(C):
            if field[i][j] == 0:
                if is_valid(i, j, field):
                    return
    
    return 1
    

def is_valid(x, y, field):
    while x < R:
        if field[x][y]:
            return 1
        x += 1


blocks = {
    1: [[0, 0], [0, 1], [0, 2], [0, 3]],
    2: [[0, 0], [0, 1], [1, 0], [1, 1]],
    3: [[0, 0], [1, 0], [1, 1], [1, 2]],
    4: [[0, 1], [1, 1], [1, 0], [2, 0]],
    5: [[0, 0], [1, 0], [1, 1], [2, 0]],
    6: [[0, 0], [1, 0], [2, 0], [2, 1]],
    7: [[0, 1], [0, 0], [1, 0], [2, 0]],
}

C, P = map(int, input().split())
floor = list(map(int, input().split()))
R = max(floor) + 4
cnt = 0
ans = []

# 0도
blocks[P].sort()

for i in range(C - blocks[P][-1][0]):
    arr = [[x+i, y] for x, y in blocks[P]]
    if when_block_is_down(arr):
        ans.append(arr)

# 90도
for x, y in blocks[P]:
    blocks_90 = [[y, blocks[P][-1][0]-x] for x, y in blocks[P]]

blocks_90.sort()
for i in range(C - blocks_90[-1][0]):
    arr = [[x+i, y] for x, y in blocks_90]
    if when_block_is_down(arr):
        ans.append(arr)


# 180도
for x, y in blocks[P]:
    blocks_180 = [[blocks[P][-1][0]-x, max(blocks[P], key=lambda x: x[1])[1]-y] for x, y in blocks[P]]

blocks_180.sort()
for i in range(C - blocks_180[-1][0]):
    arr = [[x+i, y] for x, y in blocks_180]
    if when_block_is_down(arr):
        ans.append(arr)

# 270도
for x, y in blocks[P]:
    blocks_270 = [[max(blocks[P], key=lambda x: x[1])[1]-y, x] for x, y in blocks[P]]

blocks_270.sort()
for i in range(C - blocks_270[-1][0]):
    arr = [[x+i, y] for x, y in blocks_270]
    if when_block_is_down(arr):
        ans.append(arr)

new_ans = []
for v in ans:
    if v not in new_ans:
        new_ans.append(v)

print(len(new_ans))