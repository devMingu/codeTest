import heapq
n = int(input())
idx = 0
h = []
answer = 0
while n:
    member = int(input())
    if idx != 0:
        heapq.heappush(h, [-1*member, idx])
    else:
        value = member
    idx += 1
    n -= 1


while h:
    if -1*value >= h[0][0]:
        buy, idx = heapq.heappop(h)
        buy += 1
        value += 1
        answer += 1
        heapq.heappush(h, [buy, idx])
    else:
        break

print(answer)



