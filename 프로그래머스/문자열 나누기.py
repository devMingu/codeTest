def solution(s):
    answer = 0

    s = list(s)

    x = s[0]
    n = len(s)
    x_cnt = 1
    other_cnt = 0

    for i in range(1, n):
        if x_cnt == 0 and other_cnt == 0:
            x = s[i]

        if x == s[i]:
            x_cnt += 1
        else:
            other_cnt += 1

        if x_cnt == other_cnt:
            answer += 1
            x_cnt = 0
            other_cnt = 0

    if x_cnt > 0:
        answer += 1

    return answer