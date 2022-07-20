#편의시설은 정수값에 위치
#가장 가까운 편의시설 & 가장 먼 편의시설의 거리의 평균이 최소.

n = int(input())
store = []
for i in range(n):
    x,y = map(int, input().split())
    store.append([x,y])

max_length = 10**12
idx = 0
for i in range(n):
    m = 0
    for j in range(n):
        if j == i:
            continue
        temp = ((store[i][0] - store[j][0])**2 + (store[i][1] - store[j][1])**2) ** 0.5
        m = max(m, temp)

    if m < max_length:
        max_length = m
        idx = i


print(store[idx][0], store[idx][1])

