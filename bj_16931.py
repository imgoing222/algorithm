# 16931 겉넓이 구하기
# 다른 사람들 풀이를 보니까 두개씩 비교해서 abs값을 더했다
# 그렇게 하면 왼쪽에서 볼때랑 오른쪽에서 볼때를 한번에 해결 가능! + 뒤집을 필요도 없어
# 똑똑한 사람들..............

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def area(arr):
    res = 0
    for r in arr:
        res += r[0]
        for i in range(1, len(r)):
            if r[i-1] < r[i]:
                res += r[i] - r[i-1]
    return res

N, M = map(int, input().split())
left_blocks = [list(map(int, input().split())) for _ in range(N)]
right_blocks = []
for r in left_blocks:
    right_blocks.append(list(reversed(r)))
back_blocks = list(map(list, zip(*left_blocks)))
front_blocks = []
for r in back_blocks:
    front_blocks.append(list(reversed(r)))

ans = 0

# 위/아래
ans += 2 * N * M

# 양 옆
ans += area(left_blocks)
ans += area(right_blocks)

# 앞 뒤
ans += area(front_blocks)
ans += area(back_blocks)

print(ans)

