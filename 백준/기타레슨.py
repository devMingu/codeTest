def add_lesson():
    cnt = 0
    sum_lesson = 0
    for i in range(n):
        if sum_lesson + ray[i] > mid:
            cnt += 1
            sum_lesson = 0

        sum_lesson += ray[i]
    else:
        if sum_lesson:
            cnt += 1
    return cnt


n, m = map(int, input().split())
ray = list(int(x) for x in input().split())

end = sum(ray)
start = max(ray)

while start <= end:
    mid = (start+end)//2
    cnt = add_lesson()

    if cnt <= m:
        end = mid - 1

    elif cnt > m:
        start = mid + 1

print(start)

