case = int(input())

for _ in range(case):
    clothes = {}
    typeList = []
    answer = 0
    n = int(input())
    for _ in range(n):
        wear, clothesType = input().split(' ')
        if clothesType not in clothes:
            clothes[clothesType] = [wear]
            typeList.append(clothesType)
        else:
            clothes[clothesType].append(wear)

    tmp = 1
    for el in typeList:
        tmp *= (len(clothes[el]) + 1)
    answer += tmp - 1
    print(answer)
