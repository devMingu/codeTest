def dfs(depth):
    if depth == k:
        result.add(''.join(map(str, tmp)))
        return

    for i in range(n):
        if check[i]:
            continue

        tmp.append(cards[i])
        check[i] = 1
        dfs(depth+1)
        tmp.pop()
        check[i] = 0


n = int(input())
k = int(input())
check = [0] * 100
cards = []
result = set()
tmp = []
for _ in range(n):
    card = int(input())
    cards.append(card)

dfs(0)
print(len(result))




# join 함수 이용
# a = [1,2,3,4,5]
# b = ['a','b','c']
#
# print("".join(map(str, a)))
# print("".join(map(str, b)))