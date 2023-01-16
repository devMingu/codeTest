# m, n = map(int, input().split())
# s = [[0] * m for _ in range(n)]
#
# row = 0
# column = -1
# cnt = 0
#
# row_s = n
# col_s = m
# step = 1
#
# while (row_s and col_s):
#     for i in range(col_s):
#         column += step
#         cnt += 1
#         s[row][column] = cnt
#
#     row_s -= 1
#
#     for i in range(row_s):
#         row += step
#         cnt += 1
#         s[row][column] = cnt
#
#     col_s -= 1
#     step = -step
#
# for i in range(n):
#     for j in range(m):
#         print("%3d" %(s[i][j]), end=' ')
#     print()

from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if matrix[nx][ny] == 0:
                continue

            if matrix[nx][ny] == 1:
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append((nx, ny))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())

matrix = []

for i in range(n):
    matrix.append(list(map(int, input())))


bfs(0, 0)
print(matrix[n-1][m-1])
