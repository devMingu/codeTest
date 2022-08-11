# import sys
# sys.setrecursionlimit(100000)
#
# def dfs(x, y):
#     global cnt
#     if x <= -1 or x >= n or y <= -1 or y >= m:
#         return cnt
#
#     if graph[x][y] == 'O' and not visited[x][y]:
#         graph[x][y] = 'X'
#         visited[x][y] = True
#         dfs(x-1, y)
#         dfs(x, y-1)
#         dfs(x+1, y)
#         dfs(x, y+1)
#         return cnt
#     elif graph[x][y] == 'P':
#         cnt += 1
#         graph[x][y] = 'X'
#         visited[x][y] = True
#
#     return cnt
#
#
#
#
#
# n, m = map(int, input().split())
#
# graph = []
# cnt = 0
# check = 0
# visited = [[False]*(m) for _ in range(n)]
# for _ in range(n):
#     x = list(input())
#     graph.append(x)
#
# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == 'I':
#             graph[i][j] = 'O'
#             answer = dfs(i,j)
#             if answer:
#                 print(cnt)
#             else:
#                 print('TT')
#             check = 1
#             break
#
#     if check == 1:
#         break
#
#

from collections import deque

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    cnt = 0
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >=n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 'X':
                continue

            if (graph[nx][ny] == 'O' or graph[nx][ny] == 'I' or graph[nx][ny] == 'P') and visited[nx][ny] == False:
                if graph[nx][ny] == 'P':
                    cnt += 1
                graph[nx][ny] = 'X'
                visited[nx][ny] = True
                queue.append((nx, ny))

    return cnt

n, m = map(int, input().split())

graph = []

visited = [[False]*(m) for _ in range(n)]
for _ in range(n):
    x = list(input())
    graph.append(x)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'I':
            answer = bfs(i, j)
            if answer:
                print(answer)
            else:
                print('TT')
            break
