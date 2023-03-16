from collections import deque


def bfs(x, y, new_maps, visited):
    visited[x][y] = True
    q = deque([])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q.append((x, y))

    count = int(new_maps[x][y])

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= len(new_maps) or ny < 0 or ny >= len(new_maps[0]):
                continue

            if new_maps[nx][ny] != "X" and visited[nx][ny] == False:
                visited[nx][ny] = True
                q.append((nx, ny))
                count += int(new_maps[nx][ny])

    return count


def solution(maps):
    answer = []

    new_maps = []
    n = len(maps[0])
    visited = [[False] * n for _ in range(len(maps))]

    for el in maps:
        new_maps.append(list(el))

    for i in range(len(new_maps)):
        for j in range(n):
            if new_maps[i][j] != "X" and visited[i][j] == False:
                answer.append(bfs(i, j, new_maps, visited))

    if len(answer) == 0:
        answer.append(-1)

    answer.sort()
    return answer