def solution(dartResult):
    dartResult = list(dartResult)
    a = []
    tmp = ""
    for el in dartResult:
        tmp += el
        if el == 'D' or el == 'S' or el == 'T':
            if el == 'S':
                n = int(tmp[:len(tmp)-1])
            elif el == 'D':
                n = int(tmp[:len(tmp) - 1]) ** 2
            else:
                n = int(tmp[:len(tmp) - 1]) ** 3
            a.append(n)
            tmp = ""
        elif el == '#' or el == '*':
            a.append(tmp)
            tmp = ""
    print(a)
    idx = 0
    while idx < len(a):
        if a[idx] == '#':
            a[idx-1] *= -1
            a.pop(idx)
        elif a[idx] == '*':
            if idx - 1 >= 0:
                a[idx-1] *= 2
            if idx - 2 >= 0:
                a[idx-2] *= 2
            a.pop(idx)
        else:
            idx += 1

    answer = sum(a)
    print(answer)
    return answer


# solution("1S2D*3T")
solution("1S*2T*3S")
# solution("1D2S0T")
# solution("1D#2S*3S")
# solution("1D2S3T*")


