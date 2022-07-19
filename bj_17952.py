import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
n = 0
stack = []
ans = 0
### while 말고 for로 접근 / 바로 pop 하지 말고 stack[-1] 사용해서 접근할 것
while n < N:
    hw = list(map(int, input().split()))
    # 받은 input 길이가 1이라면 (0인 경우)
    if len(hw) == 1:
        if stack:
            x = stack.pop() # pop
            x[2] -= 1       # 시간에서 1 빼주기
            if x[2] == 0:   # 0초 되면
                ans += x[1] # 점수에 합산
            else:
                stack.append(x) # 아니라면 시간 1 빼준 리스트 다시 append
    else:
        hw[2] -= 1  # 과제 이미 시작했으므로 시간에서 1 빼주기
        if hw[2] == 0:  # 0초 되면
            ans += hw[1]   # 합산
        else:
            stack.append(hw) # 0초 아니면 stack에 append
    n += 1
    
print(ans)