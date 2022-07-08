def leftSchedule(card, maxIdx):
    point = maxIdx - 1
    ans = 0
    while point > -1:
        ans += (card[maxIdx] + card[point])
        point -= 1
    return ans

def rightSchedule(card, maxIdx):
    point = maxIdx + 1
    ans = 0
    while point < len(card):
        ans += (card[maxIdx] + card[point])
        point += 1
    return ans



def solution():
    n = int(input())
    card = list(int(x) for x in input().split())

    #가장 큰 값을 기준으로 좌 우
    maxIdx = card.index(max(card))
    answer = 0
    answer += leftSchedule(card, maxIdx)
    answer += rightSchedule(card, maxIdx)
    print(answer)
    return answer

solution()


