n = int(input())
m = int(input())

res =[m]  # 0분째 터널 안 차의 수

for i in range(n):
    x, y = map(int, input().split())
    m = m + x - y
    res.append(m)

if min(res) < 0:
    print(0)
else:
    print(max(res))