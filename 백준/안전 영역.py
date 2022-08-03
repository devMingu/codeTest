# from collections import deque
# import copy
# def bfs(x,y, rainLevel):
#     queue = deque()
#     queue.append((x,y))
#
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if nx < 0 or nx >= n or ny < 0 or ny >= n:
#                 continue
#
#             if matrix[nx][ny] <= rainLevel:
#                 continue
#             else:
#                 queue.append((nx, ny))
#                 matrix[nx][ny] = rainLevel
#     return 1
#
#
# n = int(input())
# matrix = []
# minLevel = 101
# maxLevel = 0
# idx = 0
# for _ in range(n):
#     x = list(map(int, input().split()))
#     minLevel = min(minLevel, min(x))
#     maxLevel = max(maxLevel, max(x))
#     matrix.append(x)
#
# copyMatrix = copy.deepcopy(matrix)
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# area = 0
# answer = 0
# minLevel -= 1
# while minLevel < maxLevel:
#     for i in range(n):
#         for j in range(n):
#             if matrix[i][j] > minLevel:
#                 area += bfs(i, j, minLevel)
#
#     answer = max(answer, area)
#     matrix = copy.deepcopy(copyMatrix)
#     area = 0
#     minLevel += 1
#
# print(answer)

from collections import deque
import copy
def bfs(x,y, rainLevel):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if matrix[nx][ny] <= rainLevel or visited[nx][ny] == 1:
                continue
            else:
                queue.append((nx, ny))
                visited[nx][ny] = 1

    return 1


n = int(input())
matrix = []
minLevel = 101
maxLevel = 0
for _ in range(n):
    x = list(map(int, input().split()))
    minLevel = min(minLevel, min(x))
    maxLevel = max(maxLevel, max(x))
    matrix.append(x)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

area = 0
answer = 0
minLevel -= 1
while minLevel < maxLevel:
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if matrix[i][j] > minLevel and visited[i][j] == 0:
                area += bfs(i, j, minLevel)
    answer = max(answer, area)
    area = 0
    minLevel += 1

print(answer)



