def solution(citations):
    citations.sort(reverse=True)
    answer = 0
    flag = 0
    for idx in range(len(citations)):
        if idx >= citations[idx]:
            answer = idx
            flag = 1
            break

    if flag != 1:
        answer = len(citations)

    print(answer)
    return answer


solution([4,4,4])