from collections import deque
def bfs(graph, start):
    visted_nodes = []
    adjacency_nodes = deque([start])
    while adjacency_nodes:
        node = adjacency_nodes.popleft()
        if node not in visted_nodes:
            visted_nodes.append(node)
            adjacency_nodes.extend(graph[node])

    return visted_nodes


def dfs(graph, start, visted = []):
    visted.append(start)
    for node in graph[start]:
        if node not in visted:
            dfs(graph, node, visted)
    return visted


visted = []
graph = {}
n, m, v = map(int, input().split())
for _ in range(m):
    a, b = map(int, input().split())
    if a not in graph:
        graph[a] = [b]
    else:
        graph[a].append(b)
    if b not in graph:
        graph[b] = [a]
    else:
        graph[b].append(a)

for el in graph:
    graph[el].sort()

ans1 = dfs(graph, v, visted)
ans2 = bfs(graph, v)

for el in ans1:
    print(el , end=' ')
print()
for el in ans2:
    print(el, end=' ')

