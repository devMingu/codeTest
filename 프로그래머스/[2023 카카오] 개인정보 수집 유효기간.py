def makeDate(year, month, day):
    return int(year) * 12 * 28 + int(month) * 28 + int(day)


def solution(today, terms, privacies):
    answer = []

    termsObj = {}
    expireDate = []
    for el in terms:
        el = el.split(' ')
        termsObj[el[0]] = el[1]

    for el in privacies:
        el = el.split(' ')
        tmp = el[0].split('.')

        day = makeDate(tmp[0], tmp[1], tmp[2]) + (int(termsObj[el[1]]) * 28) - 1
        expireDate.append(day)

    tD = today.split('.')
    tDay = makeDate(tD[0], tD[1], tD[2])

    idx = 1
    for el in expireDate:
        if el < tDay:
            answer.append(idx)
        idx += 1

    return answer


# 날짜를 모두 day로 바꿔서 푸는게 이 문제의 핵심!