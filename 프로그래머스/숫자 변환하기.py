from collections import deque


def bfs(v, y, n, visited):
    visited[v] = 1

    q = deque([])
    q.append(v)

    dv = [n, 2, 3]

    while q:
        v = q.popleft()

        for i in range(3):
            if i == 0:
                nv = v + dv[i]
            else:
                nv = v * dv[i]

            if nv < 1 or nv > y:
                continue

            if not visited[nv]:
                visited[nv] = visited[v] + 1
                if nv == y:
                    return visited[v]

                q.append(nv)
    return -1


def solution(x, y, n):
    answer = 0
    visited = [0 for _ in range(y + 1)]
    if x == y:
        answer = 0
    else:
        answer = bfs(x, y, n, visited)
    return answer