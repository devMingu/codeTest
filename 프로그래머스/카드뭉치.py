from collections import deque


def solution(cards1, cards2, goal):
    answer = ''
    tmp = ''
    cards1 = deque(cards1)
    cards2 = deque(cards2)

    for el in goal:
        answer += el
        if len(cards1) > 0 and cards1[0] == el:
            tmp += cards1.popleft()

        if len(cards2) > 0 and cards2[0] == el:
            tmp += cards2.popleft()

    if tmp == answer:
        answer = "Yes"
    else:
        answer = "No"

    return answer