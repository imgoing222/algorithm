# 2802 시계
import sys
sys.stdin = open('input.txt')

        
# 실제 시간 중 가장 작은 숫자 찾기
def real_time(time, max_n):
    for k in range(max_n+1):
       if k_is_valid(time, k):
           # k는 0부터 증가하므로 가능한 수를 발견했다면 그것이 가장 작은 수이다. 따라서 바로 return
            return k

# k라는 숫자가 될 수 있는지 체크
def k_is_valid(time, k):
    for i in range(5):
        for j in range(3):
            # 시계에 불은 켜져 있지만 숫자 부분에는 불이 꺼져있다면 그 숫자는 탈락
            if time[i][j] == '#' and num_list[k][i][j] == '.':
                return 0
    return 1
    

num_string = """###  ..#  ###  ###  #.#  ###  ###  ###  ###  ### 
#.#  ..#  ..#  ..#  #.#  #..  #..  ..#  #.#  #.#
#.#  ..#  ###  ###  ###  ###  ###  ..#  ###  ###
#.#  ..#  #..  ..#  ..#  ..#  #.#  ..#  #.#  ..#
###  ..#  ###  ###  ..#  ###  ###  ..#  ###  ###
"""

# num_string의 숫자를 인덱스와 맞춰서 num_list 만들어주기
num_list = []
for i in range(10):
    arr = []
    for j in range(i, 50, 10):
        arr.append(num_string.split( )[j])
    num_list.append(arr)


# input의 숫자를 인덱스와 맞춰서 broken_clock 만들어주기
broken_clock = [['']*5 for _ in range(4)]
for i in range(5):
    arr = list(input().split( ))
    for j in range(4):
        broken_clock[j][i] += arr[j]


# 시계 첫번째 숫자 (0,1 / 2)
first = real_time(broken_clock[0], 2)

# 시계 두번째 숫자 (0~9 / 0~4)
if first == 2:
    second = real_time(broken_clock[1], 4)
else:
    second = real_time(broken_clock[1], 9)

# 시계 세번째 숫자 (0~5)
third = real_time(broken_clock[2], 5)

# 시계 네번째 숫자 (0~9)
fourth = real_time(broken_clock[3], 9)

print(f'{first}{second}:{third}{fourth}')