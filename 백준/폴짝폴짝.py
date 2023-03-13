from collections import deque

def bfs(x, y):
    visited[x][y] = True
    q = deque([])

    q.append((x, y))

    while q:
        x, y = q.popleft()
        move = matrix[x][y]

        for i in range(2):
            nx = x + dx[i]*move
            ny = y + dy[i]*move

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if visited[nx][ny] == False:
                visited[nx][ny] = True
                q.append((nx, ny))

                if nx == n - 1 and ny == n - 1:
                    return "HaruHaru"

    return "Hing"


n = int(input())

matrix = []
for _ in range(n):
    col = list(map(int, input().split()))
    matrix.append(col)

visited = [[False] * n for _ in range(n)]

dx = [1,0]
dy = [0, 1]


print(bfs(0, 0))