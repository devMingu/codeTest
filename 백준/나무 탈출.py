def dfs(graph, v, visited):
    visited[v] += 1
    for i in graph[v]:
        if not visited[i]:
            visited[i] += visited[v]
            dfs(graph, i, visited)

n = int(input())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

while n > 1:
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

    graph[a].sort()
    graph[b].sort()
    n -= 1

dfs(graph, 1, visited)

answer = sum(visited[2::]) - len(visited[2::])
print(visited, answer)
if answer % 2 == 0:
    print("NO")
else:
    print("YES")

