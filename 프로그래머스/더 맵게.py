import heapq

def solution(scoville, K):
    answer = 0
    scoville = heap_sort(scoville)  #heap sort
    while len(scoville) > 1:
        if scoville[0] >= K:
            break

        x1 = heapq.heappop(scoville)
        x2 = heapq.heappop(scoville)
        tmp = x1 + (x2 * 2)
        heapq.heappush(scoville, tmp)

        answer += 1

    if len(scoville) == 1:
        if scoville[0] < K:
            answer = -1

    return answer


def heap_sort(iterable):
    result = []
    h = []
    for el in iterable:
        heapq.heappush(h, el)

    for i in range(len(h)):
        result.append(heapq.heappop(h))

    return result


print(solution([1, 2, 3, 9, 10, 12], 7))





