def solution(N, stages):
    stages.sort()
    dic = {}
    n = len(stages)
    for stage in range(1, N + 1):
        stage_cnt = stages.count(stage)
        if n != 0:
            dic[stage] = stage_cnt / n
        else:
            dic[stage] = 0.0
        n -= stage_cnt
    answer = sorted(dic, key=lambda x: dic[x], reverse=True)

    return answer