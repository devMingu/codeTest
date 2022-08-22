from itertools import permutations
import math

def prime_number(num):
    if num == 1 or num == 0:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True


def solution(numbers):
    n = len(numbers)
    numbers = list(numbers)
    cnt = 1
    answer = []

    while cnt <= n:
        x = list(permutations(numbers, cnt))
        for el in x:
            tmp = ""
            for j in range(len(el)):
                tmp += el[j]

            res = int(tmp)
            if prime_number(res):
                answer.append(res)

        cnt += 1

    #경우의 수 1~n개의 조합
    answer = set(answer)
    print(answer)
    print(len(answer))
    return len(answer)

solution("011")