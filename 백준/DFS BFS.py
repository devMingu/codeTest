# DFS
# def dfs(graph, v, vistied):
#     vistied[v] = True
#
#     print(v, end = ' ')
#
#     for i in graph[v]:
#         if not vistied[i]:
#             dfs(graph, i, vistied)
#
# graph = [
#     [],
#     [2,3,8],
#     [1,7],
#     [1,4,5],
#     [3,5],
#     [3,4],
#     [7],
#     [2,6,8],
#     [1,7]
# ]
#
# visited = [False] * 9
#
# dfs(graph, 1, visited)



# BFS
# from collections import deque
#
# def bfs(graph, start, visited):
#     queue = deque([start])
#     visited[start] = True
#
#     while queue:
#         v = queue.popleft()
#         print(v, end= ' ')
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True
#
# graph = [
#     [],
#     [2,3,8],
#     [1,7],
#     [1,4,5],
#     [3,5],
#     [3,4],
#     [7],
#     [2,6,8],
#     [1,7]
# ]
#
# visited = [False] * 9
#
# bfs(graph, 1, visited)

# DFS
from collections import deque
def dfs(graph, v, visited):
    visited[v] = True

    print(v, end = ' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end= ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()

dfs(graph, V, visited)
print()
visited = [False] * (N+1)
bfs(graph, V, visited)





