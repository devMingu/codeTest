# def dfs(x, y):
#     if x<=-1 or x>=n or y<=-1 or y>=n:
#         return False
#
#     if apartment[x][y] == '1':
#         apartment[x][y] = '0'
#         global cnt
#         cnt += 1
#         dfs(x-1, y)
#         dfs(x, y-1)
#         dfs(x+1, y)
#         dfs(x, y+1)
#         return True
#
#     return False
#
#
#
# n = int(input())
#
# apartment = []
#
# count = 0
# cnt = 0
# for _ in range(n):
#     x = list(input())
#     apartment.append(x)
#
# answer = []
# for i in range(n):
#     for j in range(n):
#         if dfs(i,j):
#             count += 1
#             answer.append(cnt)
#             cnt = 0
#
# print(count)
# answer.sort()
# for el in answer:
#     print(el)
#
#


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

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if apartment[nx][ny] == '0':
                continue

            if apartment[nx][ny] == '1' and visited[nx][ny] == 0:
                # apartment[nx][ny] = '0'
                visited[nx][ny] = 1
                queue.append((nx, ny))
                cnt += 1

    return cnt



n = int(input())

apartment = []

count = 0
answer = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[0]*n for _ in range(n)]

for _ in range(n):
    x = list(input())
    apartment.append(x)

for i in range(n):
    for j in range(n):
        if apartment[i][j] == '1' and visited[i][j] == 0:
            count += 1
            answer.append(bfs(i, j))

answer.sort()
print(count)
for el in answer:
    print(el)



