def solution(name, yearning, photo):
    answer = []
    name_dic = {}

    for i in range(len(name)):
        name_value = name[i]
        yearning_value = yearning[i]

        name_dic[name_value] = yearning_value

    for el in photo:
        res = 0
        for item in el:
            if item in name_dic:
                res += name_dic[item]

        answer.append(res)

    return answer