import heapq
import sys
input = sys.stdin.readline
n = int(input())
arr = []
#left max_heap
left = []
#right is min_heap
right = []

for i in range(n):
    value = int(input())
    if len(left) == len(right):
        heapq.heappush(left, (-value, value))
    else:
        heapq.heappush(right, value)

    if i > 0 and left[0][1] > right[0]:
        temp1 = heapq.heappop(left)[1]
        temp2 = heapq.heappop(right)
        heapq.heappush(left, (-temp2, temp2))
        heapq.heappush(right, temp1)

    print(left[0][1])
#7 1 5 2 10 -99 7 5
