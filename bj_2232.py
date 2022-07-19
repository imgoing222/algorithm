import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
   
N = int(input())
mine = [(int(input()), idx) for idx in range(1, N+1)]
clear = [0] * (N+1)         # clear된 지뢰 체크용
ans = []

# 지뢰 파워 순서대로 정렬
s_mine = sorted(mine, reverse=True)

i = 0
while True:
    largest = s_mine[i][1]
    
    if clear[largest]:          # 이미 터진 지뢰라면 i만 증가시키기
        i += 1
    else:
        clear[largest] = 1      # 터진 지뢰 표시
        ans.append(largest)

        # 가장 큰 지뢰 기준으로 양쪽 터뜨리기
        # 왼쪽
        for j in range(largest-1, -1, -1):
            if mine[j-1][0] < mine[j][0]:       # 두개씩 비교해서 왼쪽이 작다면
                clear[mine[j-1][1]] = 1         # 왼쪽 지뢰 터뜨리기
            else:
                break
        # 오른쪽
        for k in range(largest-1, N-1):
            if mine[k][0] > mine[k+1][0]:       # 두개씩 비교해서 오른쪽이 작다면
                clear[mine[k+1][1]] = 1         # 오른쪽 지뢰 터뜨리기
            else:
                break

        i += 1                                  # 그 다음으로 큰 지뢰 찾으러 가기

        if sum(clear) == N:                     # 만약 N개 모두 터뜨렸을 시 break
            break

ans.sort()
for n in ans:
    print(n)