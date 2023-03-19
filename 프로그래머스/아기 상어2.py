from collections import deque

def bfs(x, y):
    dx = [-1, -1, -1, 1, 1, 1, 0, 0]
    dy = [0, -1, 1, 0, -1, 1, -1, 1]


    visited[x][y] = 1
    q = deque([])
    q.append((x, y))

    answer = 10000
    while q:
        x, y = q.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
                if matrix[nx][ny] == 1:
                    answer = min(answer, visited[nx][ny])

    return answer

N, M = map(int, input().split())

matrix = []

for el in range(N):
    pos = list(map(int, input().split()))
    matrix.append(pos)

visited = [[0] * M for _ in range(N)]
answer = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0:
            answer = max(answer, bfs(i, j))
            visited = [[0] * M for _ in range(N)]


print(answer - 1)