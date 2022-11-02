# 2841 외계인의 기타 연주
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, P = map(int, input().split())
guitar = [[] for _ in range(7)]
cnt = 0

for _ in range(N):
    line, fret = map(int, input().split())

    while guitar[line]:
        if guitar[line][-1] > fret:
            guitar[line].pop()
            cnt += 1
        else:
            break
    
    if fret not in guitar[line]:
        guitar[line].append(fret)
        cnt += 1

print(cnt)
