m, n = map(int, input().split())
s = [[0] * m for _ in range(n)]

row = 0
column = -1
cnt = 0

row_s = n
col_s = m
step = 1

while (row_s and col_s):
    for i in range(col_s):
        column += step
        cnt += 1
        s[row][column] = cnt

    row_s -= 1

    for i in range(row_s):
        row += step
        cnt += 1
        s[row][column] = cnt

    col_s -= 1
    step = -step

for i in range(n):
    for j in range(m):
        print("%3d" %(s[i][j]), end=' ')
    print()
