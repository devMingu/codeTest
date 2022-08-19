from collections import deque

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    answer = ""
    answer += str(graph[x][y])
    cnt = 5
    while cnt:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                continue
            else:
                answer += str(graph[nx][ny])
                queue.append((nx, ny))
        cnt -= 1
    print(answer)
    return answer



graph = []
for _ in range(5):
    x = map(int, input().split())
    graph.append(list(x))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(5):
    for j in range(5):
        bfs(i, j)
