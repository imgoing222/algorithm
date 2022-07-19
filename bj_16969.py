import sys
sys.stdin = open('input.txt')

# 번호판 형식 받기
form = input()

# c인 경우, d인 경우의 수를 dictionary에 저장
case = {'c': 26, 'd': 10}

# 첫번째 형식 값을 ans에 넣고 시작
ans = case[form[0]]

for i in range(1, len(form)):
    # 앞글자와 비교했을 때 같으면 경우의 수 -1 해서 곱하고 다르면 경우의 수만큼 곱해주기 
    if form[i-1] == form[i]:
        ans *= case[form[i]] - 1
    else:
        ans *= case[form[i]] % 1000000009
    
    # 나누면서 계산해야 빨리 연산 가능!!!!!!!!!!!!
    ans %= 1000000009

print(ans)