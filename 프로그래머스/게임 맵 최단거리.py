from collections import deque
def bfs(x, y, n, m, visited, maps, result):
    queue = deque()
    queue.append((x,y))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited[x][y] = True
    result[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if maps[nx][ny] == 1 and visited[nx][ny] == False:
                visited[nx][ny] = True
                result[nx][ny] = result[x][y] + 1
                queue.append((nx, ny))

                if nx == n-1 and ny == m-1:
                    return result[nx][ny]

    return -1





def solution(maps):
    n = len(maps)
    m = len(maps[0])

    visited = [[False]*m for _ in range(n)]
    result = [[0]*m for _ in range(n)]

    answer = bfs(0, 0, n, m, visited, maps, result)
    return answer


solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]])