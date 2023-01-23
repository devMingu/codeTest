def isDivided(storey):
    ans = 0
    while storey:
        n = storey % 10

        if n >= 6:
            storey += 10 - n
            ans += 10 - n

        elif n == 5 and (storey // 10) % 10 >= 5:
            storey += 10 - n
            ans += 10 - n

        else:
            ans += n
        storey = storey // 10

    return ans


def solution(storey):
    answer = isDivided(storey)

    return answer

# 일의자리 -> 십의 자리 -> 백의 자리