pascal = [[1], [1,1]]

n, k = map(int, input().split())
t = 2

while t < n:
    tmp = []
    tmp.append(1)
    left = 0
    right = 1
    while len(tmp) < t:
        tmp.append(pascal[t-1][left] + pascal[t-1][right])
        left += 1
        right += 1
    tmp.append(1)
    pascal.append(tmp)
    t += 1

print(pascal[n-1][k-1])