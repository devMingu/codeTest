from collections import deque

def bfs(start, end):
    queue = deque()
    queue.append(start)
    visited[start] = True
    count[start] = 1
    while queue:
        v = queue.popleft()
        if v == end:
            print(count[end] - 1)
            return
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] =  True
                count[i] = count[v] + 1
    print(-1)

a, b = map(int, input().split())

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
count = [0] * (n+1)


for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

bfs(a, b)
