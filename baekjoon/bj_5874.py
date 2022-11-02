import sys
sys.stdin = open('input.txt')

legs = input()
ans = 0

back_legs = [0]*(len(legs))
front_legs = [0]*(len(legs))

# 뒷다리 인덱스 찾아서 리스트에 넣기
for i in range(len(legs)-1):
    if legs[i] + legs[i+1] == '((':
        back_legs[i+1] += 1

# 앞다리 인덱스 찾아서 리스트에 넣기
for j in range(len(legs)-1):
    if legs[j] + legs[j+1] == '))':
        front_legs[j] += 1

# 뒷다리보다 앞에 있는 앞다리들 모두 더해주기
for k in range(len(legs)):
    if back_legs[k] == 1:
        ans += sum(front_legs[k+1:])

print(ans)

