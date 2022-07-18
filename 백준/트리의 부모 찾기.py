from collections import deque
def bfs(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                if i not in h:
                    h[i] = v

n = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
h = {}
for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


bfs(1)
for i in range(2, n+1):
    print(h[i])
