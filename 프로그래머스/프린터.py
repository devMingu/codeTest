def solution(priorities, location):
    answer = 0

    while priorities:
        answer += 1
        important = max(priorities)
        a = priorities.pop(0)


        if a < important:  # 중요도가 더 높은 문서가 존재할때.
            idx = priorities.index(important)
            if idx == location-1:
                break
            priorities.pop(idx)
            priorities.append(a)
        else:
            if location == 0:
                break

        location -= 1
        if location < 0:
            location = len(priorities) - 1
    print(answer)
    return answer


solution([2,1,3,2], 2)