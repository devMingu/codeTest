def solution(x, y, n):
    answer = 0

    while y > x:
        if y % 3 == 0 and y // 3 >= x and y % 2 == 0 and y // 2 >= x:
            if y - n >= x:
                y = min(y // 3, y // 2, y - n)
            else:
                y = min(y // 3, y // 2)

        elif y % 3 == 0 and y // 3 >= x:
            if y - n >= x:
                y = min(y // 3, y - n)
            else:
                y //= 3

        elif y % 2 == 0 and y // 2 >= x:
            if y - n >= x:
                y = min(y // 2, y - n)
            else:
                y //= 2
        else:
            y -= n

        answer += 1

    if y < x:
        answer = -1

    return answer

# 실패