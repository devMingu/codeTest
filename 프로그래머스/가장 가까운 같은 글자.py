def solution(s):
    answer = []

    s = list(s)
    dic = {}

    idx = 0
    for el in s:
        if el not in dic:
            dic[el] = idx
            answer.append(-1)
        else:
            res = idx - dic[el]
            answer.append(res)
            dic[el] = idx

        idx += 1

    return answer
