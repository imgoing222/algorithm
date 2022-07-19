import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
cnt_zero = 0

cctv_info = []
for i in range(R):
    for j in range(C):
        if board[i][j] in [1, 2, 3, 4, 5]:
            cctv_info.append((i, j, board[i][j]))
        elif board[i][j] == 0:
            cnt_zero += 1

ans = 0
#print(*cctv_info, sep='\n')


def make_dirs(case):
    if case == 0:
        return ([(-1, 0)], [(0, 1)], [(1, 0)], [(0, -1)])
    elif case == 1:
        return ([(-1, 0), (1, 0)], [(0, 1), (0, -1)])
    elif case == 2:
        return ([(-1, 0), (0, -1)], [(-1, 0), (0, 1)], [(0, 1), (1, 0)], [(1, 0), (0, -1)])
    elif case == 3:
        return ([(-1, 0), (0, 1), (1, 0)], [(-1, 0), (0, 1), (0, -1)], [(-1, 0), (1, 0), (0, -1)], [(0, 1), (1, 0), (0, -1)])
    elif case == 4:
        return [[(-1, 0), (0, 1), (1, 0), (0, -1)]]
    else:
        return None


def simul_dir(board, start_y, start_x, dir_l):
    global R, C
    checked = []
    # print(dir_l)
    for dy, dx in dir_l:
        tmp_y, tmp_x = start_y, start_x
        while True:
            #print(start_y, start_x)
            tmp_y, tmp_x = tmp_y+dy, tmp_x+dx
            if tmp_y < 0 or tmp_y >= R or tmp_x < 0 or tmp_x >= C or board[tmp_y][tmp_x] == 6:
                break
            if board[tmp_y][tmp_x] == 0:
                board[tmp_y][tmp_x] = 9
                checked.append((tmp_y, tmp_x))
    return checked


def back_simul(board, checked):
    for y, x in checked:
        board[y][x] = 0


# print(make_dirs(1))


def dfs(board, cctv_info, idx, dir, ac):
    global ans
    if len(dir) == len(cctv_info):
        ans = max(ans, ac)
        #print(*dir, ans)
        return

    cases = (4, 2, 4, 4, 1)
    case = cctv_info[idx][2]-1
    dirs_l = make_dirs(case)
    #print(f'cctv_info[idx][2] = {cctv_info[idx][2]}')
    #print(f'dirs_l = {dirs_l}')
    #print(f'case = {case}')
    for i in range(cases[case]):
        dir.append(i)
        # print(i)
        # print(dirs_l)
        # print(dirs_l[i])
        # print(i)
        checked = simul_dir(board,
                            cctv_info[idx][0], cctv_info[idx][1], dirs_l[i])
        print(*board, sep='\n')
        print()
        dfs(board, cctv_info, idx+1, dir, ac+len(checked))
        back_simul(board, checked)
        dir.pop()


dfs(board, cctv_info, 0, [], 0)

print(cnt_zero-ans)