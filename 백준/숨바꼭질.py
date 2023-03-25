from collections import deque

def bfs(v):
    visitied[v] = 1
    q = deque([])
    q.append(v)

    dx = [-1, 1, 2]
    cnt = 0
    while q:
        v = q.popleft()
        for i in range(3):
            if dx[i] == 2:
                nv = dx[i]*v
            else:
                nv = v + dx[i]

            if nv < 0 or nv >= max(x1, x2) + 10:
                continue

            if not visitied[nv]:
                if nv == x2:
                    visitied[nv] = visitied[v] + 1
                    return visitied[x2]
                visitied[nv] = visitied[v] + 1
                q.append(nv)

    return visitied[x2]

x1, x2 = map(int, input().split())
visitied = [0 for _ in range(max(x1, x2) + 10)]
answer = bfs(x1)

print(answer - 1)
