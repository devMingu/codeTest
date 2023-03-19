def find_gcd(a, b):
    while b > 0:
        a, b = b, a % b

    return a


def find_n_gcd(array):
    gcd = array[0]

    for el in array:
        gcd = find_gcd(gcd, el)

    return gcd


def check_divide(item, array):
    for el in array:
        if el % item == 0:
            return 0

    return item


def solution(arrayA, arrayB):
    answer = 0

    a = find_n_gcd(arrayA)
    b = find_n_gcd(arrayB)

    answer = max(check_divide(a, arrayB), check_divide(b, arrayA))

    return answer

# 1 최소 공약수
# 2 최소 공약수가 조건을 만족하는 녀석이 있는지