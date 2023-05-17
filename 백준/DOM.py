import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
    q = deque()
    q.append(v)

    cnt = 0

    while q:
        v = q.popleft()
        for i in range(len(graph[v])):
            if visited[v][i] == 0:
                q.append(graph[v][i])
                visited[v][i] = 1
                cnt += 1
                break

            if visited[v][i] == 1:
                return -1

    return cnt




N, M, P = map(int, input().split())

graph = [[] for _ in range(M + 1)]
visited = [[] for _ in range(M + 1)]

for _ in range(N):
    a, b = map(int, input().split())
    graph[b].append(a)
    visited[b].append(0)

print(bfs(P))