N, K = map(int, input().split())

stone = list(map(int, input().split()))
stone.sort()

weight = 0
sum = 0
for el in stone:
    sum += el * weight
    weight += 1
    if weight > K:
        weight = K

print(sum)