import sys
input = sys.stdin.readline
def addSchdule(start, end, day):
    for i in range(start, end+1):
        day[i] += 1

    return day

def inputDaySchdule(n, day):
    for _ in range(n):
        S, E = map(int, input().split())
        day = addSchdule(S, E, day)

    return day

def findDay(day):
    start = 1
    end = start
    answer = 0
    while start < 366:
        if day[start] != 0:
            end = start + 1
            end = findEndDay(end, day)
            answer += findAnswer(start, end, day)
            start = end
        start += 1
    print(answer)

def findEndDay(end, day):
    while end < 366:
        if day[end] == 0:
            break
        end += 1
    return end

def findAnswer(start, end, day):
    depth = max(day[start: end])
    length = len(day[start: end])
    return (depth * length)


def __main__():
    n = int(input())
    day = [0] * 366
    day = inputDaySchdule(n, day)
    findDay(day)

__main__()



