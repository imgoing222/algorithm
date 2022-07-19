import sys
sys.stdin = open('input.txt')

def solve():
    global ans

    # 1개 나눠줄 경우 + 2개 나눠줄 경우 + ... + K개 나눠줄 경우
    K = 1
    while True:
        res = 1
        for i in range(1, K+1):
            # 사탕 개수가 경우의 수이므로 1~K번 브랜드 사탕 수만큼 곱해주기
            if candies.count(i):
                res *= candies.count(i)
            else:
                return

        K += 1
        ans += res


N = int(input())
candies = list(map(int, input().split()))
ans = 0

solve()
print(ans)

