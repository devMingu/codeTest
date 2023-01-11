def combineWantAndNumber(want, number):
    dic = {}
    for i in range(len(want)):
        dic[want[i]] = number[i]

    return dic


def isAvailalbe(start, discount, food_dic):
    for key, value in food_dic.items():
        if value > discount[start: start + 10].count(key):
            return 0
    return 1


def solution(want, number, discount):
    answer = 0

    #   1. want와 number를 딕셔너리 형태로 묶는다.
    food_dic = combineWantAndNumber(want, number)
    #   2. start기준으로 + 10일 (start + 1)
    for start in range(len(discount) - 9):
        answer += isAvailalbe(start, discount, food_dic)
    #   3. 만들어진 구간을 기준으로 개수를 파악함.

    return answer