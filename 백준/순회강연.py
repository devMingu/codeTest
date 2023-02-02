import heapq
N = int(input())

schdule = []
for _ in range(N):
    Pay, Day = map(int, input().split())
    schdule.append([Day, Pay])

schdule.sort() # day를 기준으로 정렬해준다


h = []
# 1. 우선순위 큐를 이용해 pay를 힙에 넣어준다.
# 2. h 리스트의 길이는 날짜와 같다
# 3. 따라서, 새롭게 들어온 강의의 마지막 날짜보다 길이가 크다면 줄여주는데, 이때는 힙구조의 특성을 활용해 pop을 해준다.(가장 작은 강의료가 빠져나옴)
for el in schdule:
    heapq.heappush(h, el[1])
    if len(h) > el[0]:
        heapq.heappop(h)

print(sum(h))


# 날짜를 기준으로 아직 여유가 있으면 다시 집어넣고해야함.


