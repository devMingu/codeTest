#신뢰/ 신뢰하지 않
#컴퓨터 N개, M개의 줄
from collections import deque
def bfs(start):
    queue = deque([start])
    visited = [False] * (n + 1)
    visited[start] = True
    cnt = 0
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                cnt += 1

    return cnt

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    # graph[a].append(b)
    graph[b].append(a)

answer = []

for i in range(1, n+1):
    res = bfs(i)
    answer.append(res)

max_cnt = max(answer)

for i in range(n):
    if max_cnt == answer[i]:
        print(i+1, end = ' ')





