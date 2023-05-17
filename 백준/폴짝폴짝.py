from collections import deque

def bfs(v, a, b):
    q = deque()
    q.append(v)

    while q:
        q = q.popleft()





N = int(input())
bridge = list(map(int, input().split()))
a, b = map(int, input().split())

visited = [0 for _ in range(N + 1)]

print(visited)

