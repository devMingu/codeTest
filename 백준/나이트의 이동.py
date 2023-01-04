# from collections import deque
# def bfs(x,y):
#     queue = deque()
#     queue.append((x,y))
#
#     matrix[x][y] = 1
#     while queue:
#         x, y = queue.popleft()
#
#         if x == e_x and y == e_y:
#             return (matrix[e_x][e_y] - 1)
#         for i in range(8):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or nx >= l or ny < 0 or ny >= l:
#                 continue
#             if matrix[nx][ny] == 0: # 0이 아니라는 의미는 해당 위치에서 출발할 체스말이 있다는 의미. 따라서 굳이 1개 이상의 말들이 중복될 이유가 없음.
#                 matrix[nx][ny] = matrix[x][y] + 1
#                 queue.append((nx, ny))
#
#
# n = int(input())
# while n:
#     l = int(input())
#     s_x, s_y = map(int, input().split())
#     e_x, e_y = map(int, input().split())
#
#     matrix = [[0]*l for _ in range(l)]
#     dx = [-2, -2, -1, 1, -1, 1, 2, 2]
#     dy = [-1, 1, -2, -2, 2, 2, 1, -1]
#     answer = bfs(s_x, s_y)
#     print(answer)
#     n -= 1


from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x,y))

    matrix[x][y] = 1

    while queue:
        x, y = queue.popleft()

        if x == toX and y == toY:
            return (matrix[toX][toY] - 1)

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= size or ny < 0 or ny >= size:
                continue
            if matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append((nx, ny))


N = int(input())

while N:
    size = int(input())
    fromX, fromY = map(int, input().split())
    toX, toY = map(int, input().split())

    matrix = [[0]*size for _ in range(size)]
    dx = [-2, -2, -1, 1, -1, 1, 2, 2]
    dy = [-1, 1, -2, -2, 2, 2, 1, -1]
    answer = bfs(fromX, fromY)
    print(answer)
    N -= 1



