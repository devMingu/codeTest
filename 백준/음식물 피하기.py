# import sys
# sys.setrecursionlimit(10000)
#
# def dfs(x, y): # x는 행 y는 열
#     if x <= -1 or x >= n or y <= -1 or y >= m:
#         return False
#
#     if matrix[x][y] == '#':
#         matrix[x][y] = '.'
#         global cnt
#         cnt += 1
#         dfs(x-1, y)
#         dfs(x+1, y)
#         dfs(x, y-1)
#         dfs(x, y+1)
#         return True
#
#     return False
#
# n, m, k = map(int, input().split())
#
# matrix = [['.']*(m) for _ in range(n)]
#
# for _ in range(k):
#     r, c = map(int, input().split())
#     matrix[r-1][c-1] = '#'
#
# answer = 0
# cnt = 0
# for i in range(n):
#     for j in range(m):
#         if matrix[i][j] == '#':
#             if dfs(i, j):
#                 answer = max(answer, cnt)
#                 cnt = 0
#
# print(answer)



# BFS 풀이방법
from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    cnt = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if matrix[nx][ny] == '.':
                continue

            if matrix[nx][ny] == '#' and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))
                cnt += 1

    return cnt

n, m, k = map(int, input().split())
matrix = [['.']*(m) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0
for _ in range(k):
    r, c = map(int, input().split())
    matrix[r-1][c-1] = '#'

for i in range(n):
    for j in range(m):
        if matrix[i][j] == '#' and visited[i][j] == 0:
            x = bfs(i, j)
            answer = max(answer, x)

print(answer)


