# from collections import deque
#
# def bfs(x, y):
#     queue = deque()
#     queue.append((x, y))
#     visited[x][y] = True
#     distance[x][y] = 1
#     flag = 0
#     while queue:
#         x, y = queue.popleft()
#         for i in range(6):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if nx < 0 or nx >= n or ny < 0 or ny >= n:
#                 continue
#             if matrix[nx][ny] == 0:
#                 continue
#
#             if matrix[nx][ny] == 1 and visited[nx][ny] == False:
#                 matrix[nx][ny] = 0
#                 visited[nx][ny] = True
#                 queue.append((nx, ny))
#                 distance[nx][ny] = distance[x][y] + 1
#                 if nx == r2 and ny == c2:
#                     flag = 1
#                     break
#
#         if flag == 1:
#             break
#
#
#
#
# n = int(input())
#
# r1, c1, r2, c2 = map(int, input().split())
#
# matrix = [[1]*n for _ in range(n)]
# visited = [[False]*n for _ in range(n)]
# distance = [[0]*n for _ in range(n)]
#
# dx = [-2, -2, 0, 0, 2, 2]
# dy = [-1, 1, -2, 2, -1, 1]
#
# bfs(r1, c1)
#
# answer = distance[r2][c2] - 1
# print(answer)


