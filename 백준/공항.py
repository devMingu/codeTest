import sys
input = sys.stdin.readline

def findParent(x):
    if gate[x] == x:
        return x

    p = findParent(gate[x])
    gate[x] = p

    return p

def union(x, y):
    x = findParent(x)
    y = findParent(y)

    if x < y:
        gate[y] = x
    else:
        gate[x] = y




G = int(input())
P = int(input())

plane = []
gate = [i for i in range(G+1)]
answer = 0
for _ in range(P):
    plane.append(int(input()))

for el in plane:
    x = findParent(el)

    if x == 0:
        break
    union(x, x-1)
    answer += 1
print(answer)



# # 1~ G 게이트, P개의 비행기 (순서 O), 게이트에 도킹 X 폐쇄.
# import sys
# input = sys.stdin.readline
#
# G = int(input())
# P = int(input())
#
# plane = []
# gate = [0]*(G+1)
# for _ in range(P):
#     plane.append(int(input()))
#
# # 문제는 도킹한 비행기보다 더 작은 범위를 가지는 경우.
# # 따라서 더 작은 범위를 가질 수 있기 때문에 가장 뒤에 도킹을 시켜야함.
#
# answer = 0
# for el in plane:
#     if 0 not in gate[G-el+1:G+1]:
#         break
#     idx = gate[G-el+1:G+1].index(0) + (G-el+1)
#     gate[idx] = 1
#     answer += 1
# print(gate, answer)
# print(answer)
#
#
