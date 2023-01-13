# from collections import deque
#
# def bfs(x, y):
#     queue = deque()
#     queue.append((x,y))
#
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 continue
#             if graph[nx][ny] == 0:
#                 continue
#
#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = graph[x][y] + 1
#                 queue.append((nx, ny))
#     return graph[n-1][m-1]
#
# n, m = map(int, input().split())
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))
#
#
# dx = [-1,1, 0, 0]
# dy = [0,0,-1,1]
#
# print(bfs(0,0))



# 검은색 - 전류 차단
# 흰색 - 전류 통과

#
# def bfs(x, y):
#     queue = deque()
#     queue.append((x,y))
#     visited[x][y] = True
#
#     while queue:
#         x, y = queue.popleft()
#
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if nx < 0 or nx >= M or ny < 0 or ny >= N:
#                 continue
#
#             if matrix[nx][ny] == 1:
#                 continue
#
#             if matrix[nx][ny] == 0 and visited[nx][ny] is False:
#                 if nx == M - 1:
#                     return True
#                 matrix[nx][ny] = 1
#                 visited[nx][ny] = True
#                 queue.append((nx, ny))
#
#     return False
#
#
# M, N = map(int, input().split())
# matrix = []
# visited = [[False for _ in range(N)] for _ in range(M)]
#
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# for _ in range(M):
#     row = list(map(int, input()))
#     matrix.append(row)
#
# answer = "NO"
# for i in range(N):
#     if bfs(0, i):
#         answer = "YES"
#         break
#
# print(answer)

# import sys
# sys.setrecursionlimit(10**6)
#
# def dfs(x, y):
#     if x <= -1 or x >= M or y <= -1 or y >= N:
#         return False
#
#     if matrix[x][y] == 0 and visited[x][y] is False:
#         matrix[x][y] = 1
#         visited[x][y] = True
#         dfs(x-1, y)
#         dfs(x+1, y)
#         dfs(x, y+1)
#         dfs(x, y-1)
#         return True
#
#     return False
#
#
# M, N = map(int, input().split())
# matrix = []
# for _ in range(M):
#     row = list(map(int, input()))
#     matrix.append(row)
# visited = [[False for _ in range(N)] for _ in range(M)]
#
# for i in range(N):
#     dfs(0, i)
#
# answer = "YES" if visited[M-1].count(True) else "NO"
# print(answer)



