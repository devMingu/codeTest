def dfs(level, sign, total, target, numbers):
    global answer
    if level == len(numbers):
        if total == target:
            answer += 1
        return

    total += numbers[level] * sign
    dfs(level + 1, 1, total, target, numbers)
    dfs(level + 1, -1, total, target, numbers)


def solution(numbers, target):
    global answer
    answer = 0
    sign = [-1, 1]

    for el in sign:
        dfs(0, el, 0, target, numbers)

    return answer // 2