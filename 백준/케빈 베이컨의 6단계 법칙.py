from collections import deque

def bfs(v):
    q = deque([])
    q.append(v)

    visited = [False for _ in range(N + 1)]
    visited[v] = True
    count = 0

    result = [0 for _ in range(N+1)]

    result[v] = count
    while q:
        v = q.popleft()
        for el in friend[v]:
            if visited[el] == False:
                q.append(el)
                result[el] = result[v] + 1
                visited[el] = True


    return sum(result)



N, M = map(int, input().split())

friend = [[] for _ in range(N+1)]


for _ in range(M):
    a, b = map(int, input().split())

    if b not in friend[a]:
        friend[a].append(b)
    if a not in friend[b]:
        friend[b].append(a)


answer = [0]
for i in range(1, N+1):
    answer.append(bfs(i))

tmp = min(answer[1::])

for i in range(1, N+1):
    if tmp == answer[i]:
        print(i)
        break
