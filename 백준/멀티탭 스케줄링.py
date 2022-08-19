
n, k = map(int, input().split())
product = [int(x) for x in input().split()]

plug = []
answer = 0

for i in range(k):
    if product[i] in plug:
        continue

    if len(plug) < n:
        plug.append(product[i])
        continue


    far_idx = 0
    tmp = 0
    for el in plug:
        if el not in product[i:]:
            tmp = el
            break
        elif product[i:].index(el) > far_idx:
            far_idx = product[i:].index(el)
            tmp = el

    plug[plug.index(tmp)] = product[i]
    answer += 1

print(answer)




