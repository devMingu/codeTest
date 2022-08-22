def solution(priorities, location):
    #위치를 계속 추적을 하자.
    check = 0
    answer = 0
    while len(priorities) >= 2:
        x = priorities[0]
        maxN = max(priorities[1::])
        if x < maxN:
            #maxN의 우선순위가 더 높다.
            tmp = priorities.pop(0)
            location -= 1
            idx = priorities.index(maxN)
            if idx == location:
                check = 1
            priorities.pop(idx)
            priorities.append(tmp)
            if location < 0:
                location = len(priorities) - 1
        else:
            priorities.pop(0)
        answer += 1
        if check == 1:
            break

    print(answer)
    return answer

solution([3,2,4,1,3,5,2], 6)






