import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def make_roof_from_left(arr):
    global ans, l_high

    roof = 0

    for i in range(len(arr)):
        if arr[i] == highest_pillar:
            l_high = i
            break
        
        if arr[i] > roof:
            roof = arr[i]

        ans += roof
        i += 1

def make_roof_from_right(arr):
    global ans, r_high

    roof = 0

    for i in range(len(arr)):
        if arr[i] == highest_pillar:
            r_high = 1000 - i
            break
        
        if arr[i] > roof:
            roof = arr[i]

        ans += roof
        i += 1


N = int(input())
pillars = [0]*1001
ans = 0
l_high = r_high = 0


for _ in range(N):
    L, H = map(int, input().split())
    pillars[L] = H

highest_pillar = max(pillars)

make_roof_from_left(pillars)
make_roof_from_right(pillars[::-1])

ans += (r_high - l_high + 1) * highest_pillar

print(ans)