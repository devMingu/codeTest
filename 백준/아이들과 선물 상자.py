import heapq

def makeHeapList(array):
    h = []
    for el in array:
        heapq.heappush(h, -el)
    return h

def findAnswer(gift, student):
    for el in student:
        item = -heapq.heappop(gift)
        if not gift:
            return 0
        if item == el:
            continue
        elif item > el:
            heapq.heappush(gift, -(item - el))
        else:
            return 0

    return 1


N, M = map(int, input().split())

gift = list(map(int, input().split()))
student = list(map(int, input().split()))
gift = makeHeapList(gift)

answer = findAnswer(gift, student)
print(answer)




