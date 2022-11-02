import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def calculate(prize):
    global ans

    num_of_stickers = []
    for i in range(1, prize[0]+1):
        num_of_stickers.append(stickers[prize[i]-1])
    
    ans += min(num_of_stickers) * prize[-1]
        

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    prize = [list(map(int, input().split())) for _ in range(n)]
    stickers = list(map(int, input().split()))        

    ans = 0

    for i in range(n):
        calculate(prize[i])

    print(ans)