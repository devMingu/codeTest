# def dfs(graph, v, visited, count):
#     visited[v] = True
#     count += 1
#     if visited[b] == True:
#         print(count-1)
#         return 1
#     for i in graph[v]:
#         if not visited[i]:
#             check = dfs(graph, i, visited, count)
#             if check == 1:
#                 return 1
#     return False
#
# n = int(input())
# a, b = map(int, input().split())
# m = int(input())
# graph = [[] for _ in range(n+1)]
# visited = [False] * (n+1)
# count = 0
# for i in range(m):
#     x, y = map(int, input().split())
#     graph[x].append(y)
#     graph[y].append(x)
#
# check = dfs(graph, a, visited, count)
# if not check:
#     print(-1)
#
#
#


#BFS 풀이방법
from collections import deque

def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in family[v]:
            if not visited[i]:
                queue.append(i)
                res[i] = res[v] + 1
                visited[i] = True

    return -1





n = int(input())
x, y = map(int, input().split())
m = int(input())

family = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for i in range(m):
    a, b = map(int, input().split())
    family[a].append(b)
    family[b].append(a)

res = [0]*(n+1)

bfs(x)

if res[y] > 0:
    print(res[y])
else:
    print(-1)

