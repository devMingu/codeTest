def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    return visited.count(True) - 1


def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n + 1)]
    for el in wires:
        graph[el[0]].append(el[1])
        graph[el[1]].append(el[0])

    for r in range(1, len(graph)):
        el = graph[r]
        for i in range(len(el)):
            visited = [False for _ in range(n + 1)]
            tmp = el[i]
            el[i] = 0
            cnt = dfs(graph, r, visited)
            if answer > abs(2 * cnt - n):
                answer = abs(2 * cnt - n)
            el[i] = tmp

    return answer