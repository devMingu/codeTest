import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        visited[x][y] = True
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True

    return False

n, m = map(int, input().split())

graph = []
visited = [[False] * m for _ in range(n)]
check = 0

for _ in range(n):
    x = map(int, input())
    graph.append(list(x))

for i in range(m):
    dfs(0, i)

if visited[n-1].count(True):
    print("YES")
else:
    print("NO")



# from collections import deque
#
# def bfs(x,y):
#     queue = deque()
#     queue.append((x,y))
#     visited[x][y] = True
#     while queue:
#         x, y = queue.popleft()
#
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 continue
#
#             if graph[nx][ny] == 1:
#                 continue
#
#             if graph[nx][ny] == 0:
#                 queue.append((nx, ny))
#                 graph[nx][ny] = 1
#                 visited[nx][ny] = True
#
#
# n, m = map(int, input().split())
#
# graph = []
# visited = [[False] * m for _ in range(n)]
# check = 0
#
# for _ in range(n):
#     x = map(int, input())
#     graph.append(list(x))
#
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# for i in range(m):
#     bfs(0, i)
#
# if visited[n-1].count(True):
#     print("YES")
# else:
#     print("NO")
