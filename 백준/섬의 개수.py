#DFS 풀이방법
# import sys
# sys.setrecursionlimit(10000)
# def dfs(x, y):
#     if x<=-1 or x>=h or y<=-1 or y>= w:
#         return False
#
#     if matrix[x][y] == '1':
#         matrix[x][y] = '0'
#         dfs(x-1, y)
#         dfs(x, y-1)
#         dfs(x+1, y)
#         dfs(x, y+1)
#         dfs(x-1, y+1)
#         dfs(x-1, y-1)
#         dfs(x+1, y+1)
#         dfs(x+1, y-1)
#         return True
#     return False
#
# while True:
#     w, h = map(int, input().split())
#     if w == h == 0:
#         break
#     matrix = []
#     answer = 0
#     idx = 0
#     while idx < h:
#         pos = input().split(' ')
#         matrix.append(pos)
#         idx += 1
#
#     for i in range(h):
#         for j in range(w):
#             if matrix[i][j] == '1':
#                 if dfs(i, j) == True:
#                     answer += 1
#     print(answer)



#BFS 풀이방법
# from collections import deque
# def bfs(x,y):
#     queue = deque()
#     queue.append((x,y))
#
#     while queue:
#         x, y = queue.popleft()
#         for i in range(8):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if nx < 0 or nx >= h or ny < 0 or ny >= w:
#                 continue
#             if matrix[nx][ny] == 0:
#                 continue
#
#             if matrix[nx][ny] == '1':
#                 matrix[nx][ny] = '0'
#                 queue.append((nx, ny))
#
#     return 1
#
#
# dx = [-1, -1, -1, 1, 1, 1, 0, 0]
# dy = [-1, 0, 1, -1, 0, 1, -1, 1]
#
# while True:
#     w, h = map(int, input().split())
#     if w == h == 0:
#         break
#     matrix = []
#     answer = 0
#     idx = 0
#     while idx < h:
#         pos = input().split(' ')
#         matrix.append(pos)
#         idx += 1
#
#     for i in range(h):
#         for j in range(w):
#             if matrix[i][j] == '1':
#                 answer += bfs(i, j)
#     print(answer)

