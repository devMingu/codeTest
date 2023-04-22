def solution(ingredient):
    answer = 0

    start = 0
    n = len(ingredient)
    ok = [1, 2, 3, 1]

    one = []

    while start <= len(ingredient) - 4:
        if ingredient[start] == 1:
            one.append(start)

        if ingredient[start: start + 4] == ok:
            answer += 1
            for i in range(4):
                ingredient.pop(start)

            while one:
                tmp = one.pop()
                if tmp != start:
                    start = tmp
                    break
            continue

        start += 1

    return answer