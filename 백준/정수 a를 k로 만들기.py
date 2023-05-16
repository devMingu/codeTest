from collections import deque

def bfs():
    q = deque()
    q.append(A)

    while q:
        v = q.popleft()
        for i in range(2):
            if i == 0: # 1더하기
                if visited[v+1] == 0:
                    visited[v+1] = visited[v] + 1
                    q.append(v+1)
            else: # 2곱하기
                if v*2 <= K:
                    if visited[v*2] == 0:
                        visited[v*2] = visited[v] + 1
                        q.append(v*2)

        if visited[K] != 0:
            print(visited[K])
            break





A, K = map(int, input().split())

visited = [0 for _ in range(1000001)]

bfs()

