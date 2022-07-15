# DFS 풀이방법
# import sys
#
# sys.setrecursionlimit(10000)
#
# def dfs(x, y, N, M):
#     if x <= -1 or x >= N or y <= -1 or y >= M:
#         return False
#
#     if farmland[x][y] == 1:
#         farmland[x][y] = 0
#         dfs(x-1, y, N, M)
#         dfs(x, y-1, N, M)
#         dfs(x+1, y, N, M)
#         dfs(x, y+1, N, M)
#         return True
#     return False
#
# n = int(input())
# while n > 0:
#     answer = 0
#     M, N, K = map(int, input().split())
#     farmland = [[0]*M for _ in range(N)]
#     for i in range(K):
#         X, Y = map(int, input().split())
#         farmland[Y][X] = 1
#
#     for i in range(N):
#         for j in range(M):
#             if farmland[i][j] == 1:
#                 if dfs(i, j, N, M) == True:
#                     answer += 1
#     print(answer)
#     n -= 1


# BFS 풀이방법
from collections import deque
def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if farmland[nx][ny] == 0:
                continue

            if farmland[nx][ny] == 1:
                farmland[nx][ny] = 0
                queue.append((nx, ny))
    return 1


n = int(input())
while n > 0:
    answer = 0
    M, N, K = map(int, input().split())
    farmland = [[0]*M for _ in range(N)]
    for i in range(K):
        X, Y = map(int, input().split())
        farmland[Y][X] = 1
    dx = [-1, 1, 0, 0]
    dy = [0,0, -1, 1]

    for i in range(N):
        for j in range(M):
            if farmland[i][j] == 1:
                answer += bfs(i, j)

    print(answer)
    n -= 1
