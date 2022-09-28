def isTrue(n, ar):
    cnt = 0
    for el in ar:
        if n % el == 0:
            continue
        else:
            break
    else:
        return 1
    return 0


def solution(arr):
    answer = 1

    while True:
        if isTrue(answer, arr):
            break
        answer += 1

    return answer