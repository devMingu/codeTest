from collections import deque

def bfs(computer, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        visited[v] = True
        for i in computer[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n = int(input())
m = int(input())
computer = [[] for _ in range(n+1)]

visited = [False] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    computer[a].append(b)
    computer[b].append(a)
bfs(computer, 1, visited)

print(visited.count(True) - 1)


