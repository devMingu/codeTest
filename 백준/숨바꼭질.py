from collections import deque
def bfs(start):
    queue = deque([start])
    visited[start] = True

    answer = [0] * (n + 1)

    answer[start] = 1

    while queue:
        v = queue.popleft()
        for el in graph[v]:
            if not visited[el]:
                visited[el] = True
                queue.append(el)
                answer[el] = answer[v] + 1

    return answer

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    graph[x].sort()
    graph[y].sort()


result = bfs(1)

max_length = max(result)
print(result.index(max_length) ,max_length - 1, result.count(max_length))


