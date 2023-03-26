from collections import deque
def bfs(v):
    dx = [D, U]
    queue = deque([])
    queue.append(v)

    while queue:
        q = queue.popleft()

        for i in range(2):
            if i == 0:
                nq = q - dx[i]
            else:
                nq = q + dx[i]
            # print(nq)

            if nq < 0 or nq > F:
                continue

            if not visited[nq]:
                visited[nq] = visited[q] + 1

                if nq == G:
                    return visited[nq]

                queue.append(nq)


    return "use the stairs"




F, S, G, U, D = map(int, input().split())

visited = [0 for _ in range(F+1)]
print(bfs(S))

# F층으로 이루어진 건물
# 스타링크 회사의 위치 G층
# 강호의 위치 S층
# U만큼 업, D만큼 다운