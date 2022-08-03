from collections import deque
def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    wolf_cnt = 0
    sheep_cnt = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            if matrix[nx][ny] == '#':
                continue

            if matrix[nx][ny] == 'v' or matrix[nx][ny] == 'o' or matrix[nx][ny] == '.':
                queue.append((nx, ny))
                if matrix[nx][ny] == 'v':
                    wolf_cnt += 1
                elif matrix[nx][ny] == 'o':
                    sheep_cnt += 1
                matrix[nx][ny] = '#'

    #해당 영역에서 양이 더 많은지 늑대가 더 많은지 확인
    if wolf_cnt == 0 and sheep_cnt == 0:
        return 1
    else:
        if wolf_cnt >= sheep_cnt:
            return ['v', sheep_cnt] #해당하는 sheep_cnt만큼 감소
        else:
            return ['s', wolf_cnt]




R, C = map(int, input().split())

matrix = []
wolf = 0
sheep = 0
for _ in range(R):
    x = list(input())
    wolf += x.count('v')
    sheep += x.count('o')
    matrix.append(x)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(R):
    for j in range(C):
        if matrix[i][j] != '#':
            ans = bfs(i,j)
            if ans == 1:
                continue
            else:
                if ans[0] == 'v':
                    sheep -= ans[1]
                else:
                    wolf -= ans[1]

print(sheep, wolf)


