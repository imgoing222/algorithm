import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def getNumbers(idx):
    res = []
    for i in range(idx , idx + M):
        res.append(board[i% len(board)])
    return int(''.join((map(str, res))))

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    num_X = int(''.join((map(str, X))))
    num_Y = int(''.join((map(str, Y))))
    board = list(map(int, input().split()))

    ans = 0
    
    for i in range(len(board)):
        if board[i] >= X[0]:
            Z = getNumbers(i)
            if num_X <= Z <= num_Y:
                ans += 1
            
    print(ans)



    