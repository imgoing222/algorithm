import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

k, a, b = map(int, input().split())

if a * b > 0:
    if a > 0:
        print(b//k - (a - 1)//k)
    else:
        print(abs(a)//k - (abs(b) - 1)//k)
else:
    print(abs(a)//k + b//k + 1)