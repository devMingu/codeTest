from collections import deque


def bfs(x, y, n_x, n_y, routes, park):
    q = deque([])
    q.append((x, y))

    idx = 0

    a_x = x
    a_y = y

    while idx < len(routes):
        if len(q) == 0:
            q.append((x, y))
        x, y = q.popleft()

        loc, move = routes[idx].split()
        move = int(move)
        idx += 1
        check = 0

        if loc == "N":
            for i in range(1, move + 1):
                nx = x - i
                if nx < 0 or park[nx][y] == "X":
                    check = 1
                    break

            if check == 0:
                nx = x - move
                ny = y

        elif loc == "S":
            for i in range(1, move + 1):
                nx = x + i
                if nx >= n_x or park[nx][y] == "X":
                    check = 1
                    break
            if check == 0:
                nx = x + move
                ny = y
        elif loc == "W":
            for i in range(1, move + 1):
                ny = y - i
                if ny < 0 or park[x][ny] == "X":
                    check = 1
                    break
            if check == 0:
                nx = x
                ny = y - move

        else:  # "E"
            for i in range(1, move + 1):
                ny = y + i
                if ny >= n_y or park[x][ny] == "X":
                    check = 1
                    break
            if check == 0:
                nx = x
                ny = y + move

        if check == 0 and park[nx][ny] != "X":
            q.append((nx, ny))
            a_x = nx
            a_y = ny

    return [a_x, a_y]


def solution(park, routes):
    answer = []

    n_x = len(park)
    n_y = len(park[0])

    for i in range(n_x):
        for j in range(n_y):
            if park[i][j] == "S":
                return bfs(i, j, n_x, n_y, routes, park)

    return answer

