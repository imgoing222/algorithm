import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def shortcut(x, y):
    global cnt
    if x == N and y == M:
        return cnt
    
    if gamemap[x + 1][y] 


N, M = map(int, input().split())
gamemap = [list(map(int, input().split())) for _ in range(N)]
shortcut(1, 1)

