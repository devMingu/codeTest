def divisor(number):  # number : 16
    cnt = 0
    for i in range(1, int(number ** (1 / 2)) + 1):
        if number % i == 0:
            cnt += 1
            if i < number // i:
                cnt += 1
    return cnt


def find_divisor(num, limit, power):
    answer = 0
    for i in range(1, num + 1):
        cnt = divisor(i)
        if cnt > limit:
            answer += power
        else:
            answer += cnt

    return answer


def solution(number, limit, power):
    answer = find_divisor(number, limit, power)

    return answer