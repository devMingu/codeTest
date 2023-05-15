import sys
from collections import deque

input = sys.stdin.readline

def bfs(start, visited, graph):
    seq = 1
    visited[start] = seq
    q = deque()
    q.append(start)


    while q:
        v = q.popleft()

        for el in graph[v]:
            if not visited[el]:
                q.append(el)
                seq += 1
                visited[el] = seq




N, M, R = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

    graph[u].sort()
    graph[v].sort()

bfs(R, visited, graph)

for i in range(1, len(visited)):
    print(visited[i])

