import heapq


def find_count(tangerine):
    tanger = {}
    h = []

    for el in tangerine:
        if el not in tanger:
            tanger[el] = 1
        else:
            tanger[el] += 1

    for key, value in tanger.items():
        heapq.heappush(h, -value)

    return h


def solution(k, tangerine):
    answer = 0
    h = find_count(tangerine)

    while h:
        answer += 1
        item = heapq.heappop(h)
        k -= (-1 * item)
        if k <= 0:
            break

    return answer

# 가장 많은것부터 -> 우선순위 큐에 담을 수 있지 않을까?
# 개수부터 세야함
