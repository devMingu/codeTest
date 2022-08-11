import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(v):
    global answer
    visited[v] = True

    answer.append(v)
    for el in graph[v]:
        if not visited[el]:
            visited[el] = True
            dfs(el)


n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

answer = []
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    graph[u].sort()
    graph[v].sort()

dfs(r)

result = [0 for _ in range(n+1)]

i = 1
for el in answer:
    result[el] = i
    i += 1

for j in range(1, n+1):
    print(result[j])




