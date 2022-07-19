import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

RGB = list(map(int, input().split()))
cnt = 0

for i in range(3):
    if RGB[i] >= 3:
        cnt += RGB[i] // 3
        RGB[i] = RGB[i] % 3

if RGB.count(0) == 2:
    cnt += 1
else:
    cnt += max(RGB)

print(cnt)