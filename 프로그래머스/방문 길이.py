def moving(x, y, dirs, visited):
    nx, ny = x, y
    check = []
    aX, aY = x, y
    for pos in dirs:
        if pos == "U":
            nx -= 1

        elif pos == "D":
            nx += 1

        elif pos == "L":
            ny -= 1

        else:
            ny += 1

        if nx < 0 or nx > 10 or ny < 0 or ny > 10:
            if nx < 0 or nx > 10:
                nx = x

            if ny < 0 or ny > 10:
                ny = y
            continue

        if not [x, y, nx, ny] in check:
            visited[nx][ny] = visited[x][y] + 1
            check.append((x, y, nx, ny))
            check.append((nx, ny, x, y))
        x = nx
        y = ny

    check = set(check)
    return len(check) // 2


def solution(dirs):
    answer = 0

    visited = [[0] * 11 for _ in range(11)]
    answer = moving(5, 5, dirs, visited)

    return answer