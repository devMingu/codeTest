from collections import deque
def bfs(v):
    dx = [D, U]
    queue = deque([])
    queue.append(v)

    while queue:
        q = queue.popleft()

        for i in range(2):
            # 0칸 움직이는 버튼은 눌러도 의미가 없다.
            if dx[i] == 0:
                continue
            if i == 0:
                nq = q - dx[i]
            else:
                nq = q + dx[i]


            if nq < 1 or nq > F:
                continue

            if not visited[nq]:
                visited[nq] = visited[q] + 1

                if nq == G:
                    return visited[nq]

                queue.append(nq)


    return "use the stairs"



F, S, G, U, D = map(int, input().split())

visited = [0 for _ in range(F+1)]

# 층이 같을땐 움직일 필요가 없음
if S == G:
    print(visited[S])
else:
    print(bfs(S))

# F층으로 이루어진 건물
# 스타링크 회사의 위치 G층
# 강호의 위치 S층
# U만큼 업, D만큼 다운