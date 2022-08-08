#0 1 2 3 4 5 6 7 8 9

# 합이 최대가 되기위해서는 가장 앞서있는 수가 가장 큰 값을 가져가야함.

# 알파벳의 각 위치를 인덱스로 정하고, 해당 인덱스의 합이 작을수록(즉, 자릿수가 크다는 의미) 높은 수를 준다

alphabet = {
    'A': 0,
    'B': 0,
    'C': 0,
    'D': 0,
    'E': 0,
    'F': 0,
    'G': 0,
    'H': 0,
    'I': 0,
    'J': 0
}
result = []
first = []
n = int(input())
tmp = []
for _ in range(n):
    a = list(input())
    tmp.append(a)

    if a[0] not in first:
        first.append(a[0])


for el in tmp:
    l = len(el)
    for i in range(len(el)):
        x = el[i]
        alphabet[x] += 10**(l-1)
        l -= 1

for key, values in alphabet.items():
    result.append([key, values])

result.sort(key = lambda x : x[1], reverse=True)

for i in range(9,-1,-1):
    if result[i][0] not in first:
        t = result[i]
        result.remove(t)
        result.append(t)
        break

answer = 0
for i in range(10):
    answer += int(result[i][1]) * (9-i)

print(answer)


