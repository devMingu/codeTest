import sys
import heapq

input = sys.stdin.readline

n = int(input())

assignment = []
while n:
    d, t = map(int, input().split())
    heapq.heappush(assignment, [-t, d])
    n -= 1

first = heapq.heappop(assignment)
start = -1*first[0] - first[1]

while assignment:
    tmp = heapq.heappop(assignment)
    time = -1*tmp[0]
    day = tmp[1]

    if start >= time:
        start = time - day
    else:
        start -= day
print(start)



