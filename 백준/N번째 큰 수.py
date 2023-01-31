import heapq
n = int(input())
h = []

for _ in range(n):
    numbers = list(map(int, input().split()))
    for el in numbers:
        if len(h) >= n:
            if h[0] < el:
                heapq.heappop(h)
                heapq.heappush(h, el)
        else:
            heapq.heappush(h, el)

print(h[0])


import heapq
n = int(input())
h = []

for _ in range(n):
    numbers = list(map(int, input().split()))
    for el in numbers:
        if len(h) >= n:
            while len(h) >= n and h[0] < el:
                heapq.heappop(h)
            heapq.heappush(h, el)
        else:
            heapq.heappush(h, el)

print(h[0])