def solution(t, p):
    answer = 0
    n = len(t) - len(p) + 1
    k = len(p)
    num_p = int(p)

    for i in range(n):
        tmp = int(t[i:i + k])

        if tmp <= num_p:
            answer += 1

    return answer