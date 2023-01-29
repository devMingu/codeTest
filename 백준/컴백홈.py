def dfs(x, y, count):
    visited[x][y] = 1
    global answer
    if [x, y] == [0, m-1]:
        if count == k:
            answer += 1
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and matrix[nx][ny] == '.':
                visited[nx][ny] = 1
                dfs(nx, ny, count+1)
                visited[nx][ny] = 0


n, m, k = map(int, input().split())
matrix = []
answer = 0
visited = [[0] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(n):
    tmp = list(input())
    matrix.append(tmp)

dfs(n-1, 0, 1)
print(answer)



