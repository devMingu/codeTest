# from collections import deque
#
# def bfs(computer, start, visited):
#     queue = deque([start])
#     visited[start] = True
#     while queue:
#         v = queue.popleft()
#         visited[v] = True
#         for i in computer[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True
#
# n = int(input())
# m = int(input())
# computer = [[] for _ in range(n+1)]
#
# visited = [False] * (n+1)
#
# for i in range(m):
#     a, b = map(int, input().split())
#     computer[a].append(b)
#     computer[b].append(a)
# bfs(computer, 1, visited)
#
# print(visited.count(True) - 1)
#
#
#


def dfs(graph, v, visited):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)



def sortGraph(graph):
    for i in range(1, N + 1):
        graph[i].sort()
    return graph


N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

graph = sortGraph(graph)
dfs(graph, 1, visited)

print(visited.count(True) - 1)

