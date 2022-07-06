def change_Matrix(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            if a[i][j] == '0':
                a[i][j] = '1'
            else:
                a[i][j] = '0'

r, c = map(int, input().split())
answer = 0
a = []
b = []
for i in range(r*2):
    tmp = ""
    tmp = input()
    if(i < r):
        a.append(list(tmp))
    else:
        b.append(list(tmp))

for i in range(r-2):
    for j in range(c-2):
        if a[i][j] != b[i][j]:
            change_Matrix(i, j)
            answer += 1

if a == b:
    print(answer)
else:
    print(-1)



