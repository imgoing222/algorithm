# 3048 개미 
import sys
#sys.stdin = open('input.txt')

# 위치 바꾸기
def swap_ants():
    i = 0
    while i < len(ants)-1:
        if ants[i] in ants1 and ants[i+1] in ants2:
            ants[i], ants[i+1] = ants[i+1], ants[i]
            i += 2
        else:
            i += 1

            
N1, N2 = map(int, input().split())
ants1 = list(input())[::-1]
ants2 = list(input())
ants = ants1 + ants2
T = int(input())

for _ in range(T):
    swap_ants()

print(''.join(ants))