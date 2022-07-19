import sys
sys.stdin = open('input.txt')

op = {0: '+', 1: '-', 2: '*', 3: '/'}

def perm_of_operators(n, k):

    if n == k:
        ret = numbers[0]
        for i in range(N-1):
            if p[i] == '+':
                ret += numbers[i+1]
            elif p[i] == '-':
                ret -= numbers[i+1]
            elif p[i] == '*':
                ret *= numbers[i+1]
            elif p[i] == '/':
                if ret < 0 and numbers[i+1] > 0:
                    ret = -((-ret) // numbers[i+1])
                else:
                    ret //= numbers[i+1]

        ans.append(ret)
            
    else:
        for i in range(n):
            if visited[i] == 0:
                p[k] = operators[i]
                visited[i] = 1
                perm_of_operators(n, k+1)
                visited[i] = 0



N = int(input())
numbers = list(map(int, input().split()))
num_of_operators = list(map(int, input().split()))
operators = []

# 가지고 있는 연산자 리스트 만들기
for i in range(len(num_of_operators)):
    for _ in range(num_of_operators[i]):
        operators.append(op[i])

visited = [0]*(N-1)
p = [0]*(N-1)
ans = []

perm_of_operators(N-1, 0)


print(max(ans))
print(min(ans))
