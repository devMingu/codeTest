import sys
sys.setrecursionlimit(10**6)
def dfs(graph, v):
    global answer
    for i in graph[v]:
        if len(graph[i]) == 0:
            answer -= 1
        else:
            dfs(graph, i)

    if len(graph[v]) == 0:
        answer -= 1




N = int(input())
node = list(map(int, input().split()))
delete_node = int(input())

graph = [[] for _ in range(N)]

parent = set()
node_idx = 0
root = 0
for el in node:
    if el == -1:
        root = node_idx
        node_idx += 1
        continue
    graph[el].append(node_idx)
    parent.add(el)
    node_idx += 1

answer = N - len(parent)
# print(graph, answer)
dfs(graph, delete_node)

# print(graph[root], root)

if len(graph[root]) - 1 == 0:
    answer += 1

print(answer)

