from collections import deque
def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    cnt = 1
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if matrix[nx][ny] == 1:
                continue

            if matrix[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1

                queue.append((nx, ny))
                cnt += 1
    return cnt


def makeColor(c1, c2, r1, r2):
    for i in range(r1, r2):
        for j in range(c1, c2):
            matrix[i][j] = 1
            visited[i][j] = 1


m, n, k = map(int, input().split())
matrix = [[0]*(n) for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[0]*n for _ in range(m)]
for _ in range(k):
    c1, r1, c2, r2 = map(int, input().split())
    makeColor(c1, c2, r1, r2)

answer = []
cnt = 0
for i in range(m):
    for j in range(n):
        if matrix[i][j] == 0 and visited[i][j] == 0:
            cnt += 1
            answer.append(bfs(i, j))

print(cnt)
answer.sort()
for el in answer:
    print(el, end =' ')




