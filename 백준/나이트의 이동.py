from collections import deque
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    answer = 0
    matrix[x][y] = 1
    while queue:
        x, y = queue.popleft()
        answer += 1
        if x == e_x and y == e_y:
            return (matrix[e_x][e_y] - 1)
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= l or ny < 0 or ny >= l:
                continue
            if matrix[nx][ny] == 0: # 0이 아니라는 의미는 해당 위치에서 출발할 체스말이 있다는 의미. 따라서 굳이 1개 이상의 말들이 중복될 이유가 없음.
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append((nx, ny))


n = int(input())
chess = []

while n:
    l = int(input())
    s_x, s_y = map(int, input().split())
    e_x, e_y = map(int, input().split())

    matrix = [[0]*l for _ in range(l)]
    chess.append([s_x,s_y])
    chess.append([e_x, e_y])
    #chess idx 0에는 시작, 1에는 도달하고자하는 위치
    dx = [-2, -2, -1, 1, -1, 1, 2, 2]
    dy = [-1, 1, -2, -2, 2, 2, 1, -1]
    answer = bfs(s_x, s_y)
    print(answer)
    n -= 1



