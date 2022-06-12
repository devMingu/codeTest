def solution(p):
    n = len(p)
    i = 0
    answer = [0]*n
    while i < n:
        min_value = min(p[i:n])
        j = p.index(min_value)
        if j != i:
            temp = p[j]
            p[j] = p[i]
            p[i] = temp
            answer[i] += 1
            answer[j] += 1
        i += 1
    return answer


print(solution([2,5,3,1,4]))
