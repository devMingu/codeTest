import heapq
import sys


#중요한 아이디어. 가방에 들어갈 수 있는 모든 보석들중에서 생각하기.
input = sys.stdin.readline
n, k = map(int, input().split())
jewelry = []
for i in range(n):
    m, v = map(int, input().split())
    heapq.heappush(jewelry, [m,v])

weight = []
for i in range(k):
    weight.append(int(input()))
weight.sort()
answer = []
result = 0
for el in weight:
    while jewelry and el >= jewelry[0][0]:
        wei, pri = heapq.heappop(jewelry)
        heapq.heappush(answer, -pri)

    if answer:
        result += (-1)*heapq.heappop(answer)
print(result)

