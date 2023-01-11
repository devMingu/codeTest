def solution(order):
    answer = 0
    n = len(order)

    mainContainer = [i for i in range(1, n + 1)]
    subContainer = []
    start = 1
    idx = 0
    while start <= len(order):
        subContainer.append(start)

        while subContainer[-1] == order[idx]:
            idx += 1
            subContainer.pop()

            if len(subContainer) == 0:
                break
        start += 1

    answer = idx

    return answer