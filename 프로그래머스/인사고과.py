def solution(scores):
    answer = 1

    wanho_score_list = scores[0]
    wanho_score = sum(wanho_score_list)

    scores.sort(key=lambda x: (-x[0], x[1]))

    tmp = 0

    for el in scores:
        if wanho_score_list[0] < el[0] and wanho_score_list[1] < el[1]:
            return -1

        if tmp <= el[1]:
            if wanho_score < sum(el):
                answer += 1

            tmp = el[1]

    return answer

# import heapq
#
#
# def case_one(scores):
#     n = len(scores)
#
#     for i in range(1, n):
#         if scores[0][0] < scores[i][0] and scores[0][1] < scores[i][1]:
#             return -1
#
#     return scores
#
#
# def is_perfect(item1, item2, tmp):
#     for el in tmp:
#         if el[0] > item1 and el[1] > item2:
#             return 0
#
#     return 1
#
#
# def solution(scores):
#     answer = 0
#     scores = case_one(scores)
#
#     if scores == -1:
#         return -1
#
#     # 총합을 기준으로 우선순위 큐에 넣었음
#     h = []
#     idx = 0
#     for el in scores:
#         total = el[0] + el[1]
#         heapq.heappush(h, [-total, idx, el[0], el[1]])
#         idx += 1
#
#     # 큐에서 뽑아낸다
#     rank = 1
#     tmp = []
#     while h:
#         total, idx, item1, item2 = heapq.heappop(h)
#
#         # print(idx, item1, item2, rank)
#         if idx == 0:
#             return rank
#
#         # 모두 낮은 경우 -> tmp에 append할 필요 X
#         if is_perfect(item1, item2, tmp):
#             tmp.append([item1, item2])
#         else:
#             continue
#
#         rank += 1
#
#     # 3 8 10 11 14 16 22
#
#     return answer
#
# # 1. 두 점수가 전부 낮은지? -> 모든 직원을 대상으로 비교
# # 2. 총합 기준으로 정렬
#
#
# # 100 100
# # 99 99
# # 101 1
#
#
#


# import heapq
#
#
# def case_one(a, b, tmp1):
#     n = len(tmp1)
#
#     for el in tmp1:
#         if a < el[0] and b < el[1]:
#             return -1
#
#     return 1
#
#
# def is_perfect(item1, item2, tmp):
#     for el in tmp:
#         if el[0] > item1 and el[1] > item2:
#             return 0
#
#     return 1
#
#
# def solution(scores):
#     answer = 0
#     # scores = case_one(scores)
#
#     if scores == -1:
#         return -1
#
#     h = []
#     idx = 0
#
#     wanho_score = scores[0][0] + scores[0][1]
#
#     for el in scores:
#         total = el[0] + el[1]
#         if wanho_score <= total:
#             heapq.heappush(h, [-total, idx, el[0], el[1]])
#             idx += 1
#
#     rank = 1
#     tmp = []
#     tmp1 = []
#
#     while h:
#         total, idx, item1, item2 = heapq.heappop(h)
#
#         # print(idx, item1, item2, rank)
#         if idx == 0:
#             answer = rank
#             break
#
#         tmp1.append([item1, item2])
#         # 모두 낮은 경우 -> tmp에 append할 필요 X
#         if is_perfect(item1, item2, tmp):
#             tmp.append([item1, item2])
#         else:
#             continue
#
#         rank += 1
#
#     if case_one(scores[0][0], scores[0][1], tmp1) == -1:
#         answer = -1
#     return answer



