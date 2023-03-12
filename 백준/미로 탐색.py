from collections import deque
def bfs(x,y):
    visited[x][y] = 1
    q = deque([])

    q.append((x,y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if matrix[nx][ny] == 1 and visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1


N, M = map(int, input().split())

matrix = []
for _ in range(N):
    row = list(map(int, input()))
    matrix.append(row)

visited = [[0] * M for _ in range(N)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

bfs(0,0)
answer = visited[N-1][M-1]
print(answer)