# from collections import deque
# BFS 풀이방법
# def bfs(x, y):
#     queue = deque()
#     queue.append((x,y))
#     visited[x][y] = True
#     cnt = 1
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
#             if graph[nx][ny] == 0:
#                 continue
#
#             if graph[nx][ny] == 1 and visited[nx][ny] == False:
#                 cnt += 1
#                 queue.append((nx, ny))
#                 graph[nx][ny] = 0
#                 visited[nx][ny] = True
#     return cnt
#
#
# n, m = map(int , input().split())
# graph = []
# visited = [[False]*m for _ in range(n)]
#
# for _ in range(n):
#     x = map(int, input().split())
#     graph.append(list(x))
#
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# maxPaint = 0
# numOfPaint = 0
# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == 1 and visited[i][j] == False:
#             numOfPaint += 1
#             maxPaint = max(maxPaint, bfs(i, j))
#
# print(numOfPaint)
# print(maxPaint)



# DFS 풀이방법
import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    global cnt
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == 1 and visited[x][y] == False:
        graph[x][y] = 0
        visited[x][y] = True
        cnt += 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return cnt

    return False



n, m = map(int , input().split())
graph = []
visited = [[False]*m for _ in range(n)]

numOfPaint = 0
maxPaint = 0
cnt = 0
for _ in range(n):
    x = map(int, input().split())
    graph.append(list(x))


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == False:
            numOfPaint += 1
            maxPaint = max(maxPaint, dfs(i, j))
            cnt = 0

print(numOfPaint)
print(maxPaint)