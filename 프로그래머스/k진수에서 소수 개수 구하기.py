import math


def is_prime_number(x):
    if x <= 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False  # 소수가 아님
    return True  # 소수임


def tenToK(n, k):
    tmp = ''
    while n > 0:
        tmp += str(n % k)
        n //= k

    return tmp[::-1]


def solution(n, k):
    tmp = tenToK(n, k)
    answer = 0

    for el in tmp.split('0'):
        if not el:
            continue
        else:
            if is_prime_number(int(el)):
                answer += 1

    return answer