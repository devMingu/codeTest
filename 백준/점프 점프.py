# from collections import deque
#
# def bfs(v):
#     visited[v] = True
#     queue = deque([])
#     queue.append(v)
#
#     answer = 0
#     while queue:
#         pos = queue.popleft()
#         jump = [i for i in range(cage[pos], 0, -1)]
#
#         answer += 1
#         # print(pos)
#         for el in jump:
#             next = pos + el
#             if next >= n:
#                 continue
#             if cage[next] != 0:
#                 queue.append(next)
#                 visited[next] = True
#                 if visited[-1] == True:
#                     return answer
#
#     return answer
# n = int(input())
#
# cage = list(map(int, input().split()))
# visited = [False for _ in range(n)]
#
# answer = bfs(0)
# # print(cage, visited)
# print(answer)
import sys
sys.setrecursionlimit(10000)

def dfs(x):
    if x <= -1 or x >= n:
        return False

    if visited[x] == False:
        visited[x] = True
        dfs(x - arr[x])
        dfs(x + arr[x])
        return True

    return False



n = int(input())
arr = [int(x) for x in input().split()]
s = int(input())

visited = [False] * n
dfs(s-1)
answer = visited.count(True)
print(answer)


