import sys
sys.setrecursionlimit(10**6)

def dfs(x, y, tmp):
    if x < 0 or x >= H or y < 0 or y >= W:
        return 0

    if grid[x][y] == "#":
        grid[x][y] = "."
        tmp += 1
        dfs(x, y-1, tmp)
        dfs(x, y+1, tmp)
        dfs(x-1, y, tmp)
        dfs(x+1, y, tmp)
        return tmp

    return 0

n = int(input())

while n:
    H, W = map(int, input().split())
    grid = []
    cnt = 0
    visited = [[False] * W for _ in range(H)]
    for _ in range(H):
        el = list(input())
        grid.append(el)
    for i in range(H):
        for j in range(W):
            tmp = 0
            if grid[i][j] == "#":
                cnt += dfs(i, j, tmp)

    print(cnt)
    n -= 1
