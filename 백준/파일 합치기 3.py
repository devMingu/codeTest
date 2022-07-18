import heapq
import sys

input = sys.stdin.readline
def solution(chapter):
    h = []
    x1 = 0
    x2 = 0
    result = 0
    for el in chapter:
        heapq.heappush(h, el)

    while len(h) > 2:
        x1 = heapq.heappop(h)
        x2 = heapq.heappop(h)
        result += (x1 + x2)
        heapq.heappush(h, x1+x2)

    result += sum(h)
    return result

n = int(input())

while n:
    k = int(input())
    chapter = [int(x) for x in input().split()]
    answer = solution(chapter)
    print(answer)
    n -= 1
