import heapq
N = int(input())

schdule = []
for _ in range(N):
    Pay, Day = map(int, input().split())
    schdule.append([Day, Pay])
schdule.sort()


h = []
for el in schdule:
    heapq.heappush(h, el[1])
    if len(h) > el[0]:
        heapq.heappop(h)

print(sum(h))


# 날짜를 기준으로 아직 여유가 있으면 다시 집어넣고해야함.


