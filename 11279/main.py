import sys
import heapq

input = sys.stdin.readline

def heap_sort(iterable):
    h = []
    result = 0
    for value in iterable:
        heapq.heappush(h, value)
    if len(h) >= 2:
        while len(h) > 1:
            temp1 = heapq.heappop(h)
            temp2 = heapq.heappop(h)

            result += (temp1 + temp2)
            heapq.heappush(h, temp1 + temp2)

    return result

n = int(input())
iterable = []
result = 0
for _ in range(n):
    iterable.append(int(input()))

res = heap_sort(iterable)
print(res)


