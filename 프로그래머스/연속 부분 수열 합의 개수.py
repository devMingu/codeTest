
def solution(elements):
    answer = []

    for i in range(len(elements)):
        cnt = 0
        start = i
        tmp = 0
        while cnt < len(elements):
            tmp += elements[start]
            answer.append(tmp)
            start += 1
            start %= len(elements)
            cnt += 1

    answer = set(answer)
    answer = list(answer)


    #   연속되어있는 수열을 만들기 위해 수열 뒤에 붙이자.


    # 1. 만들 수 있는 경우의 수 (1 ~ len(elements))
    # 2. 각 경우의 수 별로 나올 수 있는 수 계산.
    return len(answer)