def solution(n):
    answer = 1

    tmp = n // 2 if n % 2 == 0 else n // 2 + 1

    for i in range(tmp, 1, -1):
        x = i
        res = 0
        while x:
            res += x
            if res > n:
                break
            if res == n:
                answer += 1
                break

            x -= 1

    return answer