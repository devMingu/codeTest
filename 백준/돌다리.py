from collections import deque
def bfs(x):
    queue = deque()
    queue.append(x)
    visited[x] = True

    while queue:
        v = queue.popleft()

        for i in range(8):
            if i < 6:
                x =  v + dx[i]

                if 0<= x <= 100000 and visited[x] == False:
                    queue.append(x)
                    visited[x] = True
                    graph[x] = graph[v] + 1
            else:
                x = v * dx[i]
                if 0<= x <= 100000 and visited[x] == False:
                    queue.append(x)
                    visited[x] = True
                    graph[x] = graph[v] + 1



a, b, n, m = map(int, input().split())

dx = [-1, 1, a, -a, b, -b, a, b]
visited = [False] * (100001)
graph = [0] * (100001)

bfs(n)
print(graph[m])