while True:
    try:
        s = input()
    
        n, k = map(int, s.split())
        res = n
        
        while True:
            res += n // k
            n = n // k + n % k
            if n < k:      
                break  
        print(res)

    except EOFError:
        break

#효전님 코드

import sys
#sys.stdin = open('input.txt')
input = sys.stdin.readline

for line in sys.stdin:
    n, k = map(int, line.split())
    res = 0
    stamp = 0
    while n != 0:
        res += n
        stamp += n
        n = stamp//k
        stamp %= k
    print(res)