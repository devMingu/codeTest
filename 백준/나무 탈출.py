#PyPy3로 돌려야함.
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(start):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            depth[i] = depth[start] + 1
            dfs(i)

n = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
depth = [0] * (n+1)
leafNode = []

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)
answer = 0
for i in range(2, n+1):
    if len(graph[i]) == 1:
        answer += (depth[i])



if answer % 2 == 0:
    print("No")
else:
    print("Yes")






#리프노드를 찾는방법? 루트노드에서 출발해서 끝지점에 위치한 요소들.


# import sys
# sys.setrecursionlimit(100000)
# input = sys.stdin.readline
#
# def dfs(start):
#     visited[start] += 1
#     for i in graph[start]:
#         if not visited[i]:
#             visited[i] += visited[start]
#             dfs(i)
#
# n = int(input())
#
# graph = [[] for _ in range(n+1)]
# visited = [0] * (n+1)
# leafNode = []
#
# for _ in range(n-1):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
# dfs(1)
# answer = 0
# for i in range(2, n+1):
#     if len(graph[i]) == 1:
#         answer += (visited[i]-1)
#
#
#
# if answer % 2 == 0:
#     print("No")
# else:
#     print("Yes")
#
#
#



#리프노드를 찾는방법? 루트노드에서 출발해서 끝지점에 위치한 요소들.

