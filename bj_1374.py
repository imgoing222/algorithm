import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

N = int(input())
time = []
for _ in range(N):
    num, start, end = map(int, input().split())
    time.append([start, end])

time = deque(sorted(time, key=lambda x: x[1]))

max_room = 0

for t in range(time[-1][1] + 1):
    room = 0
    for s, e in time:
        if s <= t <= e:
            room += 1
    
    while time:
        if time[0][1] == t:
            time.popleft()
        else:
            break

    max_room = max(max_room, room)

print(max_room)