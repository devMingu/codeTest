import heapq

def convert_hours_to_minutes(time):
    hours, minute = time.split(':')

    hours = int(hours)
    minute = int(minute)

    return hours * 60 + minute

def solution(plans):
    answer = []
    h = []
    wait = []

    for el in plans:
        lecture, start_time, how_long_time = el[0], el[1], el[2]
        start_time = convert_hours_to_minutes(start_time)
        end_time = int(el[2]) + start_time

        heapq.heappush(h, [start_time, end_time, el[0]])

    print(h)

    # 시작 시간을 결정
    start, end, lec = heapq.heappop(h)

    while h:
        next = h[0] # 다음번 실행할 함수.

        if end <= next[0]: # 다음번 과제보다 일찍 끝나거나 알맞게 끝나는 경우
            # 알맞게 끝나는 경우 next를 실행
            if end == next[0]:
                answer.append(lec)

            # 일찍 끝나는 경우 -> 남은 시간을 고려해서 대기상태에 있는 애들 실행.
            else:
                answer.append(lec)
                # 남는 시간이 얾마인지 계산
                remain_time = next[0] - end
                while wait:
                    if remain_time <= 0:
                        break

                    tmp = wait[-1]
                    if tmp[0] <= remain_time:
                        wait_t, wait_lec = wait.pop()
                        answer.append(wait_lec)
                        remain_time -= wait_t

                    else:
                        wait[-1][0] -= remain_time
                        remain_time = 0
            start, end, lec = heapq.heappop(h)
            if not h:
                answer.append(lec)
                break

        # 다 끝나지 않았는데 다음번 과제를 시작하는 경우
        else:
            wait.append([end-next[0], lec])
            start, end, lec = heapq.heappop(h)
            if not h:
                answer.append(lec)
                break

    while wait:
        a, b = wait.pop()
        answer.append(b)

    return answer