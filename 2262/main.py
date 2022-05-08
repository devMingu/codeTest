n = int(input())
rank = [int(x) for x in input().split()]
sum = 0
while len(rank) > 1:
    max_idx = rank.index(max(rank))
    #최대의 인덱스가 제일 왼쪽에 있을때.
    if max_idx == 0:
        temp = rank[max_idx] - rank[max_idx + 1]
        if temp < 0:
            temp *= -1
    #최대의 인덱스가 제일 오른쪽에 있을때.
    elif max_idx == len(rank) - 1:
        temp = rank[max_idx] - rank[max_idx-1]
        if temp < 0:
            temp *= -1
    #양 옆에 비교할 수가 있을때.
    else:
        temp1 = rank[max_idx] - rank[max_idx-1]
        temp2 = rank[max_idx] - rank[max_idx + 1]
        if temp1 < 0 or temp2 < 0:
            if temp1 < 0:
                temp1 *= -1
            if temp2 < 0:
                temp2 *= -1
        if temp1 > temp2:
            temp = temp2
        else:
            temp = temp1
    sum += temp
    rank.pop(max_idx)

print(sum)
