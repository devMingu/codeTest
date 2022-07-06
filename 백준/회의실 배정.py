import heapq

def heap_sort(iterable):
    h = []
    answer = 1
    for el in iterable:
        heapq.heappush(h, el)

    use_office = (heapq.heappop(h))
    for el in range(len(h)):
        check = (heapq.heappop(h))
        if use_office[0] <= check[1]:#끝나는 시간 <= 시작 시간
            use_office = check
            answer += 1

    return answer

n = int(input())

office = []

for i in range(n):
    start, end= map(int, input().split())
    office.append([end,start])

print(heap_sort(office))

