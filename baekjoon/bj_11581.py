import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def dfs(arr):
    print(arr, visited)

    for node in arr:

        if node == N:
            continue

        if visited[node]:
            print(node)
            print("CYCLE")
            exit()

        visited[node] = 1
        dfs(road[node])
        visited[node] = 0

N = int(input())
road = [0]

for _ in range(N-1):
    num = int(input())
    if num:
        road.append(list(map(int, input().split())))
    else:
        road.append([])

visited = [0] * N
print(road)
for i in range(1, N):
    visited[i] = 1
    dfs(road[i])
    visited[i] = 0

print("NO CYCLE")
