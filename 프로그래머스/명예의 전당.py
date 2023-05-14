import heapq


def solution(k, score):
    answer = []

    h = []

    for el in score:
        if len(h) <= k:
            heapq.heappush(h, el)

        else:
            if h[0] < el:
                heapq.heappush(h, el)

        if len(h) > k:
            heapq.heappop(h)

        answer.append(h[0])

    return answer