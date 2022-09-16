from collections import deque

def notApproach():
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                distance[i][j] = -1

def printAnswer():
    for el in distance:
        for i in range(len(el)):
            print(el[i], end=" ")
        print()

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if matrix[nx][ny] == 0:
                continue

            if matrix[nx][ny] == 1 and visited[nx][ny] == False:
                visited[nx][ny] = True
                matrix[nx][ny] = 0
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx,ny))


n, m = map(int, input().split())

matrix = []
answer = []
distance = [[0]*m for _ in range(n)]
visited = [[False]*m for _ in range(n)]

iIdx = 0
jIdx = 0
for i in range(n):
    x = list(map(int, input().split()))
    if x.count(2) == 1:
        jIdx = x.index(2)
        iIdx = i
    matrix.append(x)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

bfs(iIdx, jIdx)

notApproach()
printAnswer()

