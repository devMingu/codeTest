def solution(s):
    #     공백(+), (-)
    l = []
    s = s.split(' ')
    s = list(s)

    print(s)
    for el in s:
        l.append(int(el))
    l.sort()

    answer = ''
    answer += str(l[0])
    answer += ' '
    answer += str(l[-1])

    return answer