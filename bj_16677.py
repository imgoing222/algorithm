# 16677 악마 게임
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def is_valid():
    i = j = 0
    while j < len(w):
        if m[i] == w[j]:
            i += 1
            j += 1
        else:
            j += 1

        if i == len(m):
            word()
            break

def word():
    global ans, max_v

    gasungbi = int(g) / (len(w) - len(m))
    if max_v < gasungbi:
        max_v = gasungbi
        ans = w


m = input().rstrip()
max_v = 0
ans = ''

for _ in range(int(input())):
    w, g = input().split()
    is_valid()

if ans:
    print(ans)
else:
    print('No Jam')