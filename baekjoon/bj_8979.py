import sys
sys.stdin = open('input.txt')

def medal_count(arr):
    max_v = max(arr)
    winners = []
    for i in range(len(arr)):
        if arr[i] == max_v:
            winners.append(i+1)

    return winners




N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
new_board = list(map(list, zip(*board)))
rank = {}

#금메달 갯수 세기

gold = medal_count(new_board[1])
if len(gold) > 1:
    silver = medal_count(new_board[2])
else:
    rank[gold[0]] = 1
