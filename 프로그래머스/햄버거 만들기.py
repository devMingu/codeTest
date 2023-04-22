def is_hamburgur(ingredient, start):
    ok = [1, 2, 3, 1]

    idx = 0
    cnt = 0
    for i in range(start, start + 4):
        if ok[idx] == ingredient[i]:
            cnt += 1
        idx += 1

    if cnt == 4:
        while cnt:
            ingredient.pop(start)
            cnt -= 1

        return [ingredient, 1]

    return [ingredient, 0]


def solution(ingredient):
    answer = 0

    start = 0
    n = len(ingredient)

    while start <= len(ingredient) - 4:
        if ingredient[start] == 1:
            ingredient, result = is_hamburgur(ingredient, start)
            if result:
                answer += 1
                start -= 1
                continue
            print(ingredient)

        start += 1

    return answer