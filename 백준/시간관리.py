def play(timeList):
    lastTime = timeList.pop(0)
    time = lastTime[0] - lastTime[1]

    for item in timeList:
        if time <= item[0]:
            time -= item[1]
        else:
            time = item[0] - item[1]
    if time < 0:
        time = -1

    return time




n = int(input())

timeList = []
for _ in range(n):
    S, T = map(int, input().split())
    timeList.append([T, S])
timeList.sort(reverse=True)
# T: 걸리는 시간, S: 시간 내에 일을 처리해야하는 시간
answer = play(timeList)
print(answer)







# 1. 가장 일찍 끝내야되는 시간을 기준으로, 그 시간에 정해진 일을 끝낼 수 있는가?


