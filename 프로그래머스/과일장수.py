def solution(k, m, score):
    answer = 0

    score.sort()

    for i in range(len(score), -1, -m):
        tmp = score[i: i + m]
        if len(tmp) == m:
            answer += tmp[0] * m

    return answer