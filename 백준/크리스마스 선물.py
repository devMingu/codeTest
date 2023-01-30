import heapq
n = int(input())
h = []
while n:
    tmp = list(map(int, input().split()))
    loc = int(tmp[0])

    if loc != 0:
        for i in range(1, len(tmp)):
            heapq.heappush(h, -1*tmp[i])
    else:
        if len(h):
            print(-1*heapq.heappop(h))
        else:
            print(-1)

    n -= 1

# 가장 가치가 높은 선물을 뽑는 알고리즘 -> 우선순위 큐