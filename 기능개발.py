def solution(progresses, speeds):
    answer = []
    time = 0
    cnt = 0
    while len(progresses) > 0:
        if progresses[0] + time*speeds[0] >= 100:
            cnt += 1
            progresses.pop(0)
            speeds.pop(0)
        else:
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
            time += 1
    answer.append(cnt)


    return answer

print(solution([93,30,55], [1,30,5]))
print(solution([95, 90, 99, 99, 80, 99], [1,1,1,1,1,1]))