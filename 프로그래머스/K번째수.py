def solution(array, commands):
    answer = []
    for el in commands:
        i = el[0]
        j = el[1]
        k = el[2]

        tmp = array[i - 1:j]
        tmp.sort()
        answer.append(tmp[k - 1])
    return answer