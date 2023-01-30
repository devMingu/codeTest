import heapq

def solution(numbers):
    n = len(numbers)
    answer = [-1] * n

    h = []

    for i in range(n):
        while h and h[0][0] < numbers[i]:
            _, idx = heapq.heappop(h)
            answer[idx] = numbers[i]


        heapq.heappush(h, [numbers[i], i])

    return answer




