from collections import deque


def solution(queue1, queue2):
    answer = 0
    queueTotal = sum(queue1) + sum(queue2)

    if queueTotal % 2 == 0:
        avg = queueTotal // 2

        oneLength = len(queue1)
        twoLength = len(queue2)

        q1 = deque(queue1)
        q2 = deque(queue2)
        tmpQ1 = deque(queue1)
        tmpQ2 = deque(queue1)
        sum1 = 0
        sum2 = 0
        flag = 0

        for el in queue1:
            if el % 2 != 0:
                flag = 1
            sum1 += el
        for el in queue2:
            if el % 2 != 0:
                flag = 1
            sum2 += el

        if avg % 2 != 0:
            if flag == 0:
                return -1

        while sum1 != sum2:
            if answer > oneLength + twoLength + 1:
                return -1
            if sum1 < sum2:
                tmp = q2.popleft()
                sum1 += tmp
                oneLength += 1
                sum2 -= tmp
                twoLength -= 1
                q1.append((tmp))
                if twoLength == 0:
                    return -1
                if q1 == tmpQ2 and q2 == tmpQ1:
                    return -1
                answer += 1
                continue

            if sum1 > sum2:
                tmp = q1.popleft()
                sum2 += tmp
                twoLength += 1
                sum1 -= tmp
                oneLength -= 1
                q2.append((tmp))
                if oneLength == 0:
                    return -1
                if q1 == tmpQ2 and q2 == tmpQ1:
                    return -1
                answer += 1
                continue

    else:
        # 홀수일때는 합이 같을 수 없다.
        return -1

    return answer

