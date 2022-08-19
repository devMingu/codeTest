def solution(s):
    s = list(s)
    stack = []

    for el in s:
        if len(stack) == 0:
            stack.append(el)
        else:
            if stack[-1] == el:
                stack.pop()
            else:
                stack.append(el)

    if len(stack) == 0:
        answer = 1
    else:
        answer = 0

    return answer
