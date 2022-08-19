import sys
sys.setrecursionlimit(10**8)

input = sys.stdin.readline

def dfs(v):
    global cnt
    answer[v] = cnt
    visited[v] = True
    cnt += 1
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(i)


n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
answer = [0] * (n+1)
cnt = 1
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(n+1):
    graph[i].sort(reverse=True)

dfs(r)

for i in range(1, n+1):
    print(answer[i])


