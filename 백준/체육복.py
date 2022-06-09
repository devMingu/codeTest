def solution(n, lost, reserve):
    # 여유있는 학생이 lost하면 줄 수 없기에 처리해주는 코드.
    for el in lost:
        if el in reserve:
            reserve.pop(reserve.index(el))
            lost.pop(lost.index(el))
    answer = n - len(lost)
    lost.sort()
    for el in lost:
        left = el - 1
        right = el + 1
        if el == 1 or el == n:
            if el == 1:
                if right in reserve:
                    reserve.pop(reserve.index(right))
                    answer += 1
            else:
                if left in reserve:
                    reserve.pop(reserve.index(left))
                    answer += 1

        else:
            if left in reserve:
                reserve.pop(reserve.index(left))
                answer += 1
            elif right in reserve:
                reserve.pop(reserve.index(right))
                answer += 1

    return answer

res = solution(5, [4,2], [3,5])
print(res)