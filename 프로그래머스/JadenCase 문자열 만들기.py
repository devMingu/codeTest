def solution(s):
    s = list(s.lower())
    flag = 0
    answer = ''

    for el in s:
        if flag == 0 and el != ' ':
            answer += el.upper()
            flag = 1
            continue
        if el == ' ':
            flag = 0

        answer += el

    return answer

# 공백문자가 연속해서 나온다는 점에 유의!

