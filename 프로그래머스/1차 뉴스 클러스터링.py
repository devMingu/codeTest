def solution(str1, str2):
    temp1 = []
    temp2 = []
    str1 = str1.lower()
    str2 = str2.lower()
    left = 0
    right = left + 1
    while right < len(str1):
        if (str1[left] >= 'a' and str1[left] <= 'z') and (str1[right] >= 'a' and str1[right] <= 'z'):
            temp1.append(str1[left] + str1[right])
        left += 1
        right += 1

    left = 0
    right = left + 1
    while right < len(str2):
        if (str2[left] >= 'a' and str2[left] <= 'z') and (str2[right] >= 'a' and str2[right] <= 'z'):
            temp2.append(str2[left] + str2[right])
        left += 1
        right += 1


    #합집합, 교집합
    inter_cnt = 0

    tmp1_cnt = len(temp1)
    tmp2_cnt = len(temp2)
    print(temp1, temp2)
    if len(temp1) == 0 and len(temp2) == 0:
        answer = 1 * 65536
    else:
        for el in temp1:
            if temp2.count(el) != 0:
                inter_cnt += 1
                temp2.pop(temp2.index(el))

        union_cnt = tmp1_cnt + tmp2_cnt - inter_cnt
        answer = int((inter_cnt / union_cnt) * 65536)


    return answer




solution('E=M*C^2', 'e=m*c^2')