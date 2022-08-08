from collections import deque
def bfs(x, y):
    queue = deque()
    queue.append((x,y))

    sheep_cnt = 0
    wolf_cnt = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            if matrix[nx][ny] == '#':
                continue

            if visited[nx][ny] == 0:
                if matrix[nx][ny] == 'v':
                    wolf_cnt += 1
                elif matrix[nx][ny] == 'k':
                    sheep_cnt += 1
                queue.append((nx,ny))
                visited[nx][ny] = 1
    return [sheep_cnt, wolf_cnt]


r, c = map(int, input().split())

matrix = []
visited = [[0] * c for _ in range(r)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

s_c = 0
w_c = 0
for _ in range(r):
    x = list(input())
    s_c += x.count('k')
    w_c += x.count('v')

    matrix.append(x)
for i in range(r):
    for j in range(c):
        if visited[i][j] == 0:
            result = bfs(i, j)
            if result[0] <= result[1]: #늑대가 더 많을때
                s_c -= result[0]
            else:
                w_c -= result[1]


print(s_c, w_c)
