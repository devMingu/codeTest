# 1. 하루에 최대 두개


# 나누어 떨어지지 않을때 (첫번째와 마지막의 합과 첫번째와 두번째로 큰 수의 합)
# 나누어 떨어질때

n = int(input())
px = [int(x) for x in input().split()]

px.sort()
# Case 1. 나누어 떨어질때
if n % 2 == 0:
    left = 0
    right = n - 1
    max_weight = 0

    while left < right:
        tmp = px[left] + px[right]
        max_weight = max(max_weight, tmp)

        left += 1
        right -= 1

    print(max_weight)
else: # Case 2. 나누어 떨어지지 않을때 (첫번째와 마지막의 합과 첫번째와 두번째로 큰 수의 합)
    left = 0
    if (px[0] + px[n-1]) > (px[0] + px[n-2]):
        right = n - 2
        flag = 1
    else:
        right = n - 1
        flag = 0

    max_weight = 0

    while left < right:
        tmp = px[left] + px[right]
        max_weight = max(max_weight, tmp)

        left += 1
        right -= 1

    if flag == 0:
        max_weight = max(max_weight, px[left])
    else:
        max_weight = max(max_weight, px[-1])
    print(max_weight)













