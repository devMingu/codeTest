from collections import deque


def find_exit(l_x, l_y, row, col, maps):
    q = deque([])
    q.append((l_x, l_y))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited_exit = [[0] * col for _ in range(row)]
    visited_exit[l_x][l_y] = 1

    while q:
        l_x, l_y = q.popleft()

        for i in range(4):
            nx = l_x + dx[i]
            ny = l_y + dy[i]

            if nx < 0 or nx >= row or ny < 0 or ny >= col:
                continue

            if maps[nx][ny] != "X" and visited_exit[nx][ny] == 0:
                q.append((nx, ny))
                visited_exit[nx][ny] = visited_exit[l_x][l_y] + 1

    return visited_exit


def make_visited(row, col, v, value):
    for i in range(row):
        for j in range(col):
            if v[i][j] > value:
                v[i][j] = 0

    return v


def find_lever(x, y, row, col, maps):
    q = deque([])
    q.append((x, y))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited_lever = [[0] * col for _ in range(row)]
    visited_lever[x][y] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= row or ny < 0 or ny >= col:
                continue

            if maps[nx][ny] != "X" and visited_lever[nx][ny] == 0:
                q.append((nx, ny))
                visited_lever[nx][ny] = visited_lever[x][y] + 1
    return visited_lever


def solution(maps):
    answer = 0

    row = len(maps)
    col = len(maps[0])

    for i in range(row):
        if maps[i].count("S"):
            s_x = i
            s_y = maps[i].index("S")
            break

    for i in range(row):
        if maps[i].count("L"):
            row_l = i
            col_l = maps[i].index("L")
            break
    for i in range(row):
        if maps[i].count("E"):
            row_e = i
            col_e = maps[i].index("E")
            break

    v1 = find_lever(s_x, s_y, row, col, maps)
    if v1[row_l][col_l] == 0:
        return -1

    v2 = find_exit(row_l, col_l, row, col, maps)
    if v2[row_e][col_e] == 0:
        return -1

    answer = v2[row_e][col_e] + v1[row_l][col_l] - 2

    # 레버까지의 최단 경로
    # 최단 경로보다 큰 녀석들은 0으로 대체
    # 레버의 위치에서 출구 찾기

    return answer