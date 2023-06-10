def solution(r1, r2):
    answer = 0

    for x in range(1, r2 + 1):
        for y in range(1, x + 1):
            length = ((x ** 2) + (y ** 2)) ** 0.5
            if r1 <= length and length <= r2:
                if x == y:
                    answer += 4
                else:
                    answer += 8

    on_the_line = r2 - r1 + 1
    answer += on_the_line * 4

    return answer
