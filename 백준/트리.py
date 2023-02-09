import sys
sys.setrecursionlimit(10**6)
def dfs(node, delete_idx):
    node[delete_idx] = -2

    for i in range(len(node)):
        if delete_idx == node[i]:
            dfs(node, i)

N = int(input())
node = list(map(int, input().split()))
delete_node = int(input())

answer = 0
dfs(node, delete_node)
for i in range(len(node)):
    if node[i] != -2 and i not in node:
        answer += 1

print(answer)


