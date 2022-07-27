def solution(n, lost, reserve):
    idx = 0
    while idx < len(lost):
        el = lost[idx]
        if lost[idx] in reserve:
            lost.remove(el)
            reserve.remove(el)
        else:
            idx += 1
    #체육복을 도난당한 학생의 앞쪽 학생이 주는것을 우선
    #앞쪽 학생이 줄 수 없을때 뒤의 학생이 빌려줌.
    lost.sort()
    lost_cnt = len(lost)
    for el in lost:
        if (el-1) in reserve: # 앞 쪽 친구한테 빌리기
            reserve.remove(el-1)
            lost_cnt -= 1
            continue
        if (el+1) in reserve: # 뒤 쪽 친구한테 빌리기
            reserve.remove(el+1)
            lost_cnt -= 1
            continue

    answer = n - lost_cnt

    print(answer)

    return answer


solution(5, [2,4], [1,3,5])
solution(5, [2,4], [3])
solution(3, [3], [1])
solution(6, [1,2,6], [2,5])
solution(5, [2,3,4], [1,2,3])
solution(5, [2,4], [3,1])
solution(9, [5,6,8,1,2], [2,3,1,4,8,9])























# def solution(n, lost, reserve):
#     # 여유있는 학생이 lost하면 줄 수 없기에 처리해주는 코드.
#     for el in lost:
#         if el in reserve:
#             reserve.pop(reserve.index(el))
#             lost.pop(lost.index(el))
#     answer = n - len(lost)
#     lost.sort()
#     for el in lost:
#         left = el - 1
#         right = el + 1
#         if el == 1 or el == n:
#             if el == 1:
#                 if right in reserve:
#                     reserve.pop(reserve.index(right))
#                     answer += 1
#             else:
#                 if left in reserve:
#                     reserve.pop(reserve.index(left))
#                     answer += 1
#
#         else:
#             if left in reserve:
#                 reserve.pop(reserve.index(left))
#                 answer += 1
#             elif right in reserve:
#                 reserve.pop(reserve.index(right))
#                 answer += 1
#
#     return answer