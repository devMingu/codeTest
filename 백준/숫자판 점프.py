def dfs(x, y, tmp):
    if len(tmp) == 6:
        if tmp not in result:
            result.append(tmp)
        return

    if x < 0 or x >= 4 or y < 0 or y >= 4:
        return

    dfs(x-1, y, tmp+graph[x-1][y])
    dfs(x, y-1, tmp+graph[x][y-1])
    dfs(x+1, y, tmp+graph[x+1][y])
    dfs(x, y+1, tmp+graph[x][y+1])




graph = []
for i in range(5):
    n = input().split(' ')
    graph.append(n)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = []
for i in range(5):
    for j in range(5):
        dfs(i, j, graph[i][j])

print(len(result))
