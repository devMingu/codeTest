from itertools import permutations

N = int(input())    # 번호의 수 ( 0 ~ N-1 )
P = [int(x) for x in input().split()] # 각 번호별 비용
M = int(input())    # 가지고 있는 돈 M원


# 1 ~ N까지의 구간에서의 최소
# 0 ~ N까지의 구간에서의 최소


# a == b or b == 0
if N > 1:
    a = P.index(min(P[1::]))
    b = P.index(min(P))
    if a == 0 and b == 0:
        a += 1

    k = 0
    answer = []

    if P[a] > M:
        print(0)
    else:
        M -= P[a]
        answer.append(a)
        tmp = (M // P[b])
        M -= (P[b]*tmp)
        # a~b~ 가득찬 상태에서 바꿔줄수 있는 숫자들로 바꾸기.

        for i in range(tmp):
            answer.append(b)

        i = N-1
        while True:
            if M >= (P[i] - P[answer[k]]) and i > answer[k]:
                M -= (P[i] - P[answer[k]])
                answer[k] = i
                k += 1
            else:
                i -= 1

            if i <= 0 or k >= len(answer):
                break

        for el in answer:
            print(el, end='')
else:
    print(0)











