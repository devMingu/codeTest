from collections import deque
import sys
input = sys.stdin.readline
def bfs(v):
    q = deque([])
    q.append(v)
    visited[v] = 0
    while q:
        v = q.popleft()

        for el in graph[v]:
            if visited[el] == -1:
                visited[el] = visited[v] + 1
                q.append(el)

def make_graph(N):
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        A, B = map(int, input().split())
        graph[A].append(B)

    return graph

N, M, K, X = map(int, input().split())

graph = make_graph(N)
visited = [-1 for _ in range(N+1)]
bfs(X)

# print(visited)

if visited.count(K):
    for i in range(1, N+1):
        if K == visited[i]:
            print(i)
else:
    print(-1)

