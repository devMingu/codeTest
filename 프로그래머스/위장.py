def solution(clothes):
    h = {}
    itemList = []
    answer = 1
    for items in clothes:
        # itemName = items[0]
        itemType = items[1]
        if itemType not in h:
            h[itemType] = 1
        else:
            h[itemType] += 1

    for key, item in h.items():
        # print(key, item)
        answer *= (item+1)
    answer -= 1
    # print(answer)
    return answer


solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])
# solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])