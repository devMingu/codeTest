import heapq


def convert_hours_to_minutes(time):
    hours, minute = time.split(':')

    hours = int(hours)
    minute = int(minute)

    return hours * 60 + minute


def solution(plans):
    answer = []
    h = []

    for el in plans:
        lecture, start_time, how_long_time = el[0], el[1], el[2]
        start_time = convert_hours_to_minutes(start_time)
        end_time = int(el[2]) + start_time

        heapq.heappush(h, [start_time, end_time, el[0]])

    print(h)

    start, end, lec = heapq.heappop(h)

    tmp = []
    while len(h):
        next = h[0]
        if end <= next[0]:
            answer.append(lec)
            if end == next[0]:  # 새로운 과제
                start, end, lec = heapq.heappop(h)
            else:
                if tmp:  # 멈춘 과제가 있다면 -> 멈춘 과제 시작
                    start, end, lec = heapq.heappop(tmp)
                else:  # 멈춘 과제가 없다면 -> 새로운 과제 시작
                    start, end, lec = heapq.heappop(h)
            if len(h) == 0:
                answer.append(lec)
        else:
            heapq.heappush(tmp, [next[0], end, lec])
            start, end, lec = heapq.heappop(h)

    while tmp:
        tmp_s, tmp_e, tmp_lec = heapq.heappop(tmp)
        answer.append(tmp_lec)
    return answer


740
780
music
750
850
computer
760
810
science
840
870
history

