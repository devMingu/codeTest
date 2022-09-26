def solution(arr1, arr2):
    answer = [[]]
    j = 0
    #   A by B AND C ny D == AC by BD
    for el in arr1:
        tmp = 0
        k = 0
        while k < len(arr2[0]):
            for i in range(len(arr2)):
                tmp += el[i] * arr2[i][k]
            answer[j].append(tmp)
            tmp = 0
            k += 1
        j += 1
        answer.append([])


    return answer[:-1]

solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]])
solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]])
