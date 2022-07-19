import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    a, b = map(list, input().split())
    a = [0] + a
    b = [0] + b
    if len(a) > len(b):
        b = [0]*(len(a)-len(b)) + b
    elif len(b) > len(a):
        a = [0]*(len(b)-len(a)) + a

    ans = ''
    c = 0
    for i in range(len(a)-1, -1, -1):
        bin_sum = int(a[i]) + int(b[i]) + c
        c = bin_sum // 2
        s = bin_sum % 2

        ans += str(s)
    
    print(int(ans[::-1]))
