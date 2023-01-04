# import heapq
# N = int(input())
# tmp = input().split(' ')
# house = []
#
# limit = 1440
# answer = 0
# for i in range(N):
#     heapq.heappush(house, -1 * int(tmp[i]))
#
# while len(house) > 1:
#     h1 = heapq.heappop(house)
#     h2 = heapq.heappop(house)
#
#     answer += 1
#     h1 += 1
#     h2 += 1
#     if h1 != 0:
#         heapq.heappush(house, h1)
#     if h2 != 0:
#         heapq.heappush(house, h2)
#
#
# if len(house) != 0:
#     answer += house[-1]
# if answer > limit:
#     answer = -1
#
# print(answer)

N = int(input())
tmp = input().split(' ')

house = []
for i in range(N):
    house.append(int(tmp[i]))

house.sort(reverse=True)
left = 0
right = 1
answer = 0
while len(house) > 1:
    house[left] -= 1
    house[right] -= 1
    answer += 1
    if house[left] == 0 or house[right] == 0:
        if house[left] == 0 and house[right] == 0:
            house.pop(left)
            house.pop(left)
        elif house[left] == 0:
            house.pop(left)
        else:
            house.pop(right)

    house.sort(reverse=True)

if len(house) != 0:
    answer += house[-1]

if answer > 1440:
    answer = -1

print(answer)


