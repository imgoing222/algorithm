import sys
#sys.stdin = open('input.txt')
from collections import deque

def bfs(x):
    Q = deque()
    Q.append(x)
    visited[x] = 1

    while Q:
        x = Q.popleft()
        print(x, end=' ')
        for w in range(N+1):
            if not visited[w] and adj[x][w] == 1:
                Q.append(w)
                visited[w] = 1


def dfs(x):
    visited[x] = 1
    print(x, end= ' ')

    for w in range(N+1):
        if not visited[w] and adj[x][w] == 1:
            visited[w] = 1
            dfs(w)


N, M, V = map(int, input().split())
adj = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    adj[s][e] = adj[e][s] = 1


visited = [0] * (N+1)
dfs(V)

print()
visited = [0] * (N+1)
bfs(V)