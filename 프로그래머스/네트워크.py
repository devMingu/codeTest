from collections import deque


def bfs(v, visited, graph):
    visited[v] = True
    q = deque([v])

    while q:
        v = q.popleft()

        idx = 0
        for el in graph[v]:
            if not visited[idx] and el == 1:
                visited[idx] = True
                q.append(idx)

            idx += 1

    return 1


def solution(n, computers):
    answer = 0

    visited = [False for _ in range(n)]

    for i in range(len(computers)):
        if not visited[i]:
            answer += bfs(i, visited, computers)

    return answer