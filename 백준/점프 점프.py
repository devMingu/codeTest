# import sys
# sys.setrecursionlimit(10000)
#
# def dfs(x):
#     if x <= -1 or x >= n:
#         return False
#
#     if visited[x] == False:
#         visited[x] = True
#         dfs(x - arr[x])
#         dfs(x + arr[x])
#         return True
#
#     return False
#
#
#
# n = int(input())
# arr = [int(x) for x in input().split()]
# s = int(input())
#
# visited = [False] * n
# dfs(s-1)
# answer = visited.count(True)
# print(answer)
#
#



