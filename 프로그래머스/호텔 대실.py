import heapq


def timeToSeconds(time):
    tmp = time.split(":")
    hours, minuts = tmp[0], tmp[1]
    
    seconds = (int(hours) * 60 * 60) + (int(minuts) * 60)
    return seconds


def makeTimeList(book_time):
    h = []
    for el in book_time:
        start, end = el[0], el[1]
        s = timeToSeconds(start)
        e = timeToSeconds(end)

        heapq.heappush(h, [s, e])
    return h


def solution(book_time):
    answer = 1
    e = []
    h = makeTimeList(book_time)

    tmp = heapq.heappop(h)
    heapq.heappush(e, tmp[1])

    while h:
        t = heapq.heappop(h)
        s_t, e_t = t[0], t[1]

        if e[0] <= s_t + 600:
            heapq.heappop(e)
        heapq.heappush(e, e_t)

    answer = len(e)

    return answer