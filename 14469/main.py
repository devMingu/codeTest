#백준 14469번 문제

n = int(input())
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append([a,b])
arr.sort()

start = 0
last = start + 1
while (last < n):
    if arr[start] == arr[last]:
        for j in range(start, n):
            if arr[start] == arr[j]:
                temp = arr[start][1]
                arr[start][1] = arr[j][1]
                arr[j][1] = temp

    start += 1
    last = start + 1

time = arr[0][0] + arr[0][1]
next = 1
while (next < n):
    if time <= arr[next][0]:
        time = arr[next][0] + arr[next][1]
    else:
        time += arr[next][1]
    next += 1
print(time)