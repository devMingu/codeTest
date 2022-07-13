def dfs(graph, v, visited, count):
    visited[v] = True
    count += 1
    if visited[b] == True:
        print(count-1)
        return 1
    for i in graph[v]:
        if not visited[i]:
            check = dfs(graph, i, visited, count)
            if check == 1:
                return 1
    return False

n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
count = 0
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

check = dfs(graph, a, visited, count)
if not check:
    print(-1)



