from collections import deque
import sys
input = sys.stdin.readline
def bfs(v):
    visited[v] = True
    q = deque([v])
    count = 0
    while q:
        count += 1
        v = q.popleft()
        answer[v] = count

        for el in graph[v]:
            if not visited[el]:
                q.append(el)
                visited[el] = True




N, M, R = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
answer = [0 for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    graph[i].sort(reverse=True)
bfs(R)
for i in range(1, N+1):
    print(answer[i])