def sortByConditionOne(data, c):
    data.sort(key=lambda x: (x[c], -x[0]))


def modByC(m, arr):
    modValue = 0
    for el in arr:
        modValue += el % m

    return modValue


def solution(data, col, row_begin, row_end):
    answer = 0
    sortByConditionOne(data, col - 1)

    tmp = []
    while row_begin <= row_end:
        tmp.append(modByC(row_begin, data[row_begin - 1]))
        row_begin += 1

    answer = tmp.pop()

    while tmp:
        answer ^= tmp.pop()

    return answer