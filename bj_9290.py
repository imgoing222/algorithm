# 9290 틱택토 이기기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def find_namkyu():
    for i in range(3):
        for j in range(3):
            if board[i][j] == nk:
                if to_win(i, j, nk):
                    return

def to_win(x, y, nk):
    # 행
    if board[x].count(nk) == 2 and board[x].count('-') == 1:
        for i in range(3):
            if board[x][i] == '-':
                board[x][i] = nk
        return 1

    # 열
    if r_board[y].count(nk) == 2 and r_board[y].count('-') == 1:
        for i in range(3):
            if board[i][y] == '-':
                board[i][y] = nk
        return 1

    # 대각선
    if x == y:  
        diagonal = []
        for i in range(3):
            for j in range(3):
                if i == j:
                    diagonal.append(board[i][j])
        
        if diagonal.count(nk) == 2 and diagonal.count('-') == 1:
            for i in range(3):
                for j in range(3):
                    if i == j and board[i][j] == '-':
                        board[i][j] = nk
            return 1

    if x + y == 2:
        diagonal = []
        for i in range(3):
            for j in range(3):
                if i + j == 2:
                    diagonal.append(board[i][j])
        
        if diagonal.count(nk) == 2 and diagonal.count('-') == 1:
            for i in range(3):
                for j in range(3):
                    if i + j == 2 and board[i][j] == '-':
                        board[i][j] = nk
            return 1


T = int(input())
for tc in range(1, T+1):
    board = [list(input().rstrip()) for _ in range(3)]
    r_board = list(map(list, zip(*board)))
    nk = input().rstrip()

    find_namkyu()

    print(f'Case {tc}:')
    for r in board:
        print(''.join(r))
