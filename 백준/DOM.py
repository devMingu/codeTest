from collections import deque

def bfs(v):
    q = deque()
    q.append(v)

    cnt = 0

    while q:
        v = q.popleft()
        for i in range(len(graph[v])):
            if graph[v][i] != 0 and hate_channel[v][i] == 0:
                q.append(graph[v][i])
                hate_channel[v][i] = 1
                cnt += 1
                break

            if hate_channel[v][i] == 1:
                return -1

    return cnt




N, M, P = map(int, input().split())

graph = [[] for _ in range(M + 1)]
hate_channel = [[] for _ in range(M + 1)]

for _ in range(N):
    a, b = map(int, input().split())
    graph[b].append(a)
    hate_channel[b].append(0)

print(bfs(P))