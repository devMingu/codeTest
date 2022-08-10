# 아군 - 흰색, 적
from collections import deque

def bfs_White(x,y):
    queue = deque()
    queue.append((x,y))
    white_cnt = 0
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            if graph[nx][ny] == 'W' and visited[nx][ny] == False:
                graph[nx][ny] = 'D'
                visited[nx][ny] = True
                white_cnt += 1
                queue.append((nx, ny))

    if white_cnt == 0: # 병사가 한명일때. 즉, 주변에 다른 병사가 없을때.
        white_cnt = 1
    return white_cnt

def bfs_Blue(x,y):
    queue = deque()
    queue.append((x,y))
    blue_cnt = 0
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            if graph[nx][ny] == 'B' and visited[nx][ny] == False:
                graph[nx][ny] = 'D'
                visited[nx][ny] = True
                blue_cnt += 1
                queue.append((nx, ny))

    if blue_cnt == 0: # 병사가 한명일때. 즉, 주변에 다른 병사가 없을때.
        blue_cnt = 1
    return blue_cnt



n, m = map(int, input().split())
graph = []
visited = [[False]*n for _ in range(m)]

# n 가로, m은 세로
for _ in range(m):
    x = input()
    tmp = []
    for el in x:
        tmp.append(el)
    graph.append(tmp)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

res = 0
answer_white = 0
answer_blue = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == 'W' and visited[i][j] == False:
            res = bfs_White(i, j)
            answer_white += res**2
        elif graph[i][j] == 'B' and visited[i][j] == False:
            res = bfs_Blue(i, j)
            answer_blue += res**2
print(answer_white, answer_blue)





