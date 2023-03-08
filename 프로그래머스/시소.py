def solution(weights):
    answer = 0
    dic = {}
    ratio = [2 / 3, 2 / 4, 3 / 4]

    for el in weights:
        if el not in dic:
            dic[el] = weights.count(el)

    for k, v in dic.items():
        answer += v * (v - 1) / 2

        for ra in ratio:
            target = k * ra
            if target in dic:
                answer += dic[target] * v
    return answer