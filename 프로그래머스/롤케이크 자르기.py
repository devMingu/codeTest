def solution(topping):
    answer = 0

    left = set()
    right = {}

    for el in topping:
        if el not in right:
            right[el] = 1
        else:
            right[el] += 1

    for el in topping:
        left.add(el)
        right[el] -= 1

        if right[el] == 0:
            del right[el]

        if len(left) == len(right.keys()):
            answer += 1

    return answer