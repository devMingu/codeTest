def cal(num, p):
    n = 10
    result = 0
    while num:
        tmp = num % n
        result += (tmp ** p)

        num //= n
    return result
a, p = map(int, input().split())
answer = [a]
idx = 0
while True:
    tmp = cal(answer[idx], p)

    if tmp not in answer:
        answer.append(tmp)
        idx += 1
    else:
        ans = answer.index(tmp)
        break

print(ans)