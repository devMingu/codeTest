# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10000)
# def dfs(start):
#     visited[start] = True
#
#     for i in (graph[start]):
#         if not visited[i]:
#             dfs(i)
#
# n, m = map(int, input().split())
#
# graph = [[] for _ in range(n+1)]
# visited = [False]*(n+1)
#
# for i in range(1, m+1):
#     x1, x2 = map(int, input().split())
#     graph[x1].append(x2)
#     graph[x2].append(x1)
#
# answer = 0
# for i in range(1, n+1):
#     if not visited[i]: #방문하지 않았을때
#         dfs(i)
#         answer += 1
#
# print(answer)
import sys
from collections import deque
input = sys.stdin.readline
def bfs(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for i in range(1, m+1):
    x1, x2 = map(int, input().split())
    graph[x1].append(x2)
    graph[x2].append(x1)

answer = 0
for i in range(1, n+1):
    if not visited[i]: #방문하지 않았을때
        bfs(i)
        answer += 1
print(answer)