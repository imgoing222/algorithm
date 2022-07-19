import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

tc = 1

while True:
    N = int(input())
    if N == 0:
        break
    
    board = [list(map(int, input().split())) for _ in range(N)]
    
    board[0][0] = 987654321
    board[0][2] += board[0][1]

    calc_board = []

    # 계산 보드 초기화
    calc_board.append(board[0])
    for i in range(N-1):
        calc_board.append([0, 0, 0])

    for i in range(1, N):
        for j in range(3):
            # 북서, 서
            if j == 0: 
                north_west = west = 987654321
                
            else: 
                north_west = calc_board[i-1][j-1]
                west = calc_board[i][j-1]
            # 북
            north = calc_board[i-1][j]
            # 북동
            if j == 2:
                north_east = 987654321
            else:
                north_east = calc_board[i-1][j+1]

            calc_board[i][j] = board[i][j] + min(north, north_east, north_west, west)

    end_point = calc_board[N-1][1]

    print(f'{tc}. {end_point}')

    tc += 1 

        

