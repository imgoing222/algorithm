import sys
#sys.stdin = open('input.txt')
from collections import deque

def bfs(x):
    Q = deque()
    Q.append(x)
    visited[x] = 1

    while Q:
        x = Q.popleft()
        for w in adj[x]:
            if not visited[w]:
                Q.append(w)
                visited[w] = 1

N = int(input())
E = int(input())
adj = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(E):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

bfs(1)

# 1번 컴퓨터 본인 제외
print(sum(visited)-1)