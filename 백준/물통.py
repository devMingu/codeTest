from collections import deque

def bfs(x,y):
    q = deque([])
    q.append((x, y))
    visited[x][y] = True

    while q:
        x, y = q.popleft()
        z = c - x - y

        if x == 0:
            answer.append(z)

        # x -> y
        water = min(x, b-y)
        nx = x - water
        ny = y + water

        if visited[nx][ny] == False:
            visited[nx][ny] = True
            q.append((nx, ny))

        # x -> z
        water = min(x, c-z)
        nx = x - water
        ny = y

        if visited[nx][ny] == False:
            visited[nx][ny] = True
            q.append((nx, ny))

        # y -> x
        water = min(y, a-x)
        nx = x + water
        ny = y - water

        if visited[nx][ny] == False:
            visited[nx][ny] = True
            q.append((nx, ny))

        # y -> z
        water = min(y, c-z)
        nx = x
        ny = y - water

        if visited[nx][ny] == False:
            visited[nx][ny] = True
            q.append((nx, ny))

        # z -> x
        water = min(z, a-x)
        nx = x + water
        ny = y

        if visited[nx][ny] == False:
            visited[nx][ny] = True
            q.append((nx, ny))

        # z -> y
        water = min(z, b-y)
        nx = x
        ny = y + water

        if visited[nx][ny] == False:
            visited[nx][ny] = True
            q.append((nx, ny))



a, b, c = map(int, input().split())

visited = [[False] * (b+1) for _ in range(a+1)]
answer = []

bfs(0, 0)

answer.sort()
for el in answer:
    print(el, end = ' ')





# x -> y
# x -> z
# y -> x
# y -> z
# z -> x
# z -> y

