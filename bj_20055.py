# 20055 컨베이어 벨트 위의 로봇
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

def move_one_step_forward():
    # last_belt = belt.pop()
    # belt.appendleft(last_belt)
    # last_robot = robot.pop()
    # robot.appendleft(last_robot)
    belt.rotate(1)
    robot.rotate(1)
    # 다른 코드 읽어보니 rotate 사용 가능!!
    # rotate(n)
    # n < 0 : 왼쪽으로 회전  /  n > 0: 오른쪽으로 회전 

def move_robot():
    global robot_num
    for idx in range(N-2, -1, -1):
        if robot[idx]:
            if robot[idx+1] == 0 and belt[idx+1] >= 1:
                robot[idx], robot[idx+1] = robot[idx+1], robot[idx]
                belt[idx+1] -= 1

def add_robot():
    if belt[0] != 0 and robot[0] == 0:
        robot[0] = 1
        belt[0] -= 1

def chk():
    if belt.count(0) >= K:
        return 1

def remove_robot():
    if robot[N-1]:
        robot[N-1] = 0

N, K = map(int, input().split()) 
belt = deque(list(map(int, input().split())))
robot = deque([0]*2*N)
cnt = 0

while True:
    cnt += 1

    move_one_step_forward()
    remove_robot()

    move_robot()
    remove_robot()

    add_robot()

    if chk():
        break

print(cnt)
