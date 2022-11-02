import sys
sys.stdin = open('input.txt')

N = int(input())
M = int(input())
vote = list(map(int, input().split()))

pic = {}

for i in range(M):
    # 딕셔너리에 후보가 없다면 추가하고 있다면 value를 1 증가
    pic.setdefault(vote[i], 0)
    pic[vote[i]] += 1
    if len(pic) == N+1:              # 딕셔너리 길이가 N+1 이라면
        del(pic[vote[i]])            # 방금 넣은거 지우고
        dic_min = min(pic.values())  # 가장 작은 값 찾기
        for key, value in pic.items():
            # 딕셔너리는 넣은 순서대로 생성되므로 앞에서부터 돌면서 가장 작은 value의 key 찾아서 지워버리기
            if value == dic_min:
                del(pic[key])
                break
        # 방금 넣었다 지웠던거 다시 추가
        pic.setdefault(vote[i], 0)
        pic[vote[i]] += 1

ans = []
for k in pic.keys():
    ans.append(k)

print(*sorted(ans))