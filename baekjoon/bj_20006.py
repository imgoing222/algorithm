# 20006 랭킹전 대기열
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

p, m = map(int, input().split())

game_rooms = []

for i in range(p):
    l, n = input().split()
    l = int(l)
 
    for room in game_rooms:

        # 레벨 제한 사이에 있고 대기열에 자리가 남아 있다면 먼저 생성된 방부터 탐색해서 넣어주기
        if room[0][0]-10 <= l <= room[0][0]+10 and len(room) <= m - 1:
            room.append([l, n])
            break
    # 아니면(break에 걸리지 않았다면) 새로운 방 생성
    else:
        game_rooms.append([[l, n]])


for room in game_rooms:
    # 인원이 꽉차면 started 아니라면 waiting
    if len(room) == m:
        print('Started!')
    else:
        print('Waiting!')

    ordered_room = sorted(room, key = lambda x: x[1])
    for player in ordered_room:
        print(*player)

