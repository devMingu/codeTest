def find(n):
    if n == 6:
        return 1
    elif n == 5:
        return 2
    elif n == 4:
        return 3
    elif n == 3:
        return 4
    elif n == 2:
        return 5
    else:
        return 6
def solution(lottos, win_nums):
    count = 0
    for el in lottos:
        if el in win_nums:
            count += 1

    zero_cnt = lottos.count(0)

    #최저의 경우

    answer = [find(count+zero_cnt), find(count)]
    print(answer)
    return answer



#기존에 정답인 횟수 + 0이 맞을 확률
#기존에 정답인 횟수 + 0이 전부 틀릴 확률
solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])
