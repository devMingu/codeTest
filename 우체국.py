n = int(input())
arr = []

count = 0
for _ in range(n):
    x, a = map(int, input().split())
    count += a
    arr.append([x,a])
arr.sort()
mid_person = count//2

if count % 2 != 0:
    mid_person += 1

temp = 0
for x, a in arr:
    temp += a
    if temp >= mid_person:
        print(x)
        break



