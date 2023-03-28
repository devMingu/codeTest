import heapq


def case_one(scores):
    n = len(scores)

    for i in range(1, n):
        if scores[0][0] < scores[i][0] and scores[0][1] < scores[i][1]:
            return -1

    return scores


def solution(scores):
    answer = 0
    scores = case_one(scores)

    if scores == -1:
        return -1

    # 총합을 기준으로 우선순위 큐에 넣었음
    h = []
    idx = 0
    for el in scores:
        total = el[0] + el[1]
        heapq.heappush(h, [-total, idx, el[0], el[1]])
        idx += 1

    # 큐에서 뽑아낸다
    rank = 1
    tmp = []
    while h:
        total, idx, item1, item2 = heapq.heappop(h)

        # print(idx, item1, item2, rank)
        if idx == 0:
            return rank

        if tmp == []:
            tmp = [item1, item2]
        else:
            if tmp[0] > item1 and tmp[0] > item2:
                continue
            if tmp[0] <= item1 or tmp[1] <= item2:
                tmp = [item1, item2]

        rank += 1

    # 3 8 10 11 14 16 22

    return answer

# 1. 두 점수가 전부 낮은지? -> 모든 직원을 대상으로 비교
# 2. 총합 기준으로 정렬


# 100 100
# 99 99
# 101 1

