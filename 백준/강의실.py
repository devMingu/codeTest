import heapq
import sys
input = sys.stdin.readline

def queue_sort():
    h = []
    e = []

    n = int(input())

    for _ in range(n):
        number, start, end = map(int, input().split())
        heapq.heappush(h, [start, end])

    print(h)
    s1, e1 = heapq.heappop(h)
    heapq.heappush(e, e1)

    while h:
        start1, end1 = heapq.heappop(h)
        print(start1, end1)
        if e[0] <= start1:
            heapq.heappop(e)
        heapq.heappush(e, end1)
    print(e)
    return len(e)
answer = queue_sort()
print(answer)

