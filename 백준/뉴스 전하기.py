# 서로다른 부모의 자식이 존재한다면 전화를 하면 된다.

n = int(input())
tree = [[] for _ in range(n)]
visited = [False] * (n)

visited[0] = True
x = list(map(int, input().split()))

for i in range(1, len(x)):
    tree[x[i]].append(i)

# tree에는 자식들의 번호가 담겨 있음.
cnt = 0
tmp = []



while True:
    max_children = -1
    for i in range(n):
        idx = 0
        if visited[i] == True:
            if len(tree[i]) > 0: # 자식이 존재하는가?
                for a in tree[i]: # 자식들을 선택해야하는 상황.
                    if max_children < len(tree[a]):
                        idx = tree[i].index(a)
                        max_children = len(tree[a])
                tmp.append(tree[i][idx])
                tree[i].pop(idx)
    for el in tmp:
        visited[el] = True
    tmp = []
    cnt += 1
    if visited.count(True) == n:
        break

print(cnt)




