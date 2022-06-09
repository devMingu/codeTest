#데드라인을 넘지 않은 상태에서 가장 높은 값을 고르자.
import heapq

n = int(input())
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append([a,b])
arr.sort()

day = arr[-1][0]
h = []
answer = 0
while day > 0:
    while arr:
        deadLine, score = arr.pop()
        if day == deadLine:
            heapq.heappush(h, -score)
        else:
            arr.append([deadLine, score])
            break
    if h:
        answer += -heapq.heappop(h)
    day -= 1

print(answer)

