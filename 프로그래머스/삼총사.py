from itertools import combinations


def solution(number):
    answer = 0
    combi = list(combinations(number, 3))

    for el in combi:
        if sum(el) == 0:
            answer += 1

    return answer