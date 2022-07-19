# 7490 0 만들기
# eval이라는 함수가 있구나....?!?!

import sys
sys.stdin = open('input.txt')
from itertools import product

def calc(ex):
    arr = ex.replace(' ', '')
    res = 0
    num = ''
    op = '+'
    for i in range(len(arr)):
        if arr[i] in operators:
            if op == '+':
                res += int(num)
            elif op == '-':
                res -= int(num)
            op = arr[i]
            num = ''
        else:
            num += arr[i]
    if op == '+':
        res += int(num)
    elif op == '-':
        res -= int(num)
            
    if res == 0:
        return 1

T = int(input())
for tc in range(T):
    N = int(input())
    operators = ['+', '-', ' ']
    ans = []

    for case in product(operators, repeat=N-1):
        ex = ''
        for i in range(N-1):
            ex += str(i+1)
            ex += case[i]
        ex += str(N)
        
        if calc(ex):
            ans.append(ex)

    for i in sorted(ans):
        print(i)

    if tc != T-1:
        print()
