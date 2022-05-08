#0을 기준으로 왼쪽은 왼쪽대로
#오른쪽은 오른쪽대로

n, m = map(int, input().split())
book_idx = [int(x) for x in input().split()]
book_idx.sort()
left = []
right = []
result = []
for el in book_idx:
    if el < 0:
        left.append(el)
    else:
        right.append(el)

if len(left) != 0:
    for i in range(0, len(left), m):
        if i % m == 0:
            result.append(left[i])

if len(right) != 0:
    for i in range(len(right)-1, -1, -m):
        result.append(right[i])

for i in range(len(result)):
    if result[i] < 0:
        result[i] *= -1

result.sort()
sum = 0
for i in range(len(result)):
    sum += result[i] * 2
    if i == len(result) - 1:
        sum -= result[i]
print(sum)

