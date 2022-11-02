a = int(input())

game =  [[0]*3 for _ in range(3)]

def compare():
    game_reverse = list(map(list, zip(*game)))
    if [1, 1, 1] in game or [1, 1, 1] in game_reverse:
        return 1
    elif [2, 2, 2] in game or [2, 2, 2] in game_reverse:
        return 2
    elif (game[0][0] == game[1][1] == game[2][2]) or (game[0][2] == game[1][1] == game[2][0]):
        return game[1][1]
    else:
        return 0

i = 1
while i < 10:
    x, y = map(int, input().split())
    if i % 2:
        game[x - 1][y - 1] = [1, 2][a > 1]
    else:
        game[x - 1][y - 1] = [2, 1][a > 1]
    res = compare()
    i += 1
    if res == 1 or res == 2:
        break

print(res)