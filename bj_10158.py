import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

x_li = [i for i in range(w)] + [j for j in range(w, 0, -1)]
y_li = [i for i in range(h)] + [j for j in range(h, 0, -1)]

x = x_li[(p + t) % len(x_li)]
y = y_li[(q + t) % len(y_li)]
print(x, y)

