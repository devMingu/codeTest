import sys
from collections import deque

input = sys.stdin.readline

def bfs(v):
    queue = deque([])
    queue.append((0,cage[0]))

    while queue:
        pos, jump = queue.popleft()

        for i in range(1, jump+1):
            next = pos + i

            if next >= n or visited[next]:
                continue

            visited[next] = visited[pos] + 1
            queue.append((next, cage[next]))

    answer = visited[-1] if visited[-1] else -1
    return answer
n = int(input())

if n == 1:
    print(0)
else:
    cage = list(map(int, input().split()))
    visited = [0] * n

    answer = bfs(0)
    print(answer)
