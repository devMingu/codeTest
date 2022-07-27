# import sys
#
# sys.setrecursionlimit(100000)
# def dfs(x,y):
#     if x<= -1 or x >= m or y <= -1 or y >= n:
#         return False
#
#     if matrix[x][y] == 1:
#         matrix[x][y] = 0
#         dfs(x-1, y)
#         dfs(x, y-1)
#         dfs(x+1, y)
#         dfs(x, y+1)
#         dfs(x-1, y-1)
#         dfs(x-1, y+1)
#         dfs(x+1, y-1)
#         dfs(x+1, y+1)
#         return True
#     return False
#
#
# m, n = map(int, input().split())
#
# matrix = []
#
# for i in range(m):
#     x = [int(x) for x in input().split()]
#     matrix.append(x)
#
# answer = 0
# for i in range(m):
#     for j in range(n):
#         if matrix[i][j] == 1:
#             if dfs(i,j) == True:
#                 answer += 1
#
# print(answer)

