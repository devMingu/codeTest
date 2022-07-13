# def case1():
#     res = 0
#     for i in range(n):
#         check1 = 0
#         left = 0
#         right = left + 1
#         while right < m:
#             if graph[i][left] == '-' and graph[i][right] == '-':
#                 check1 = 1
#                 graph[i][right] = 1
#             else:
#                 if check1 == 1:
#                     res += 1
#                     check1 = 0
#                     graph[i][left] = 1
#                 left = right
#             right += 1
#         if check1 == 1:
#             graph[i][left] = 1
#             check1 = 0
#             res += 1
#     return res
#
# def case2():
#     res = 0
#     for i in range(m):
#         check2 = 0
#         up = 0
#         down = up + 1
#         while down < n:
#             if graph[up][i] == '|' and graph[down][i] == '|':
#                 check2 = 1
#                 graph[down][i] = 1
#             else:
#                 if check2 == 1:
#                     res += 1
#                     check2 = 0
#                     graph[up][i] = 1
#                 up = down
#             down += 1
#         if check2 == 1:
#             graph[up][i] = 1
#             check2 = 0
#             res += 1
#     return res
#
# n, m = map(int , input().split())
# graph = []
#
# for i in range(n):
#     graph.append(list(input()))
#
# answer = 0
# answer += case1() + case2()
#
# #나머지 나무 판자
# for i in range(n):
#     answer += graph[i].count('-') + graph[i].count('|')
# print(answer)

def dfs(x, y):
    if graph[x][y] == '|':
        graph[x][y] = 'O'
        for _x in [1,-1]:
            X = x + _x
            if (X > 0 and X < n) and (graph[X][y] == '|'):
                dfs(X, y)

    if graph[x][y] == '-':
        graph[x][y] = 'O'
        for _y in [1, -1]:
            Y = y + _y
            if (Y>0 and Y<m) and (graph[x][Y] == '-'):
                dfs(x, Y)



n, m = map(int , input().split())
graph = []

for i in range(n):
    graph.append(list(input()))

answer = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == '-' or graph[i][j] == '|':
            dfs(i, j)
            answer += 1

print(answer)



