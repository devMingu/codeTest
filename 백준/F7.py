import sys
input = sys.stdin.readline

n = int(input())
drivers = []
answer = 0
for _ in range(n):
    drivers.append(int(input()))
drivers = sorted(drivers)

tmp = n
for i in range(len(drivers)):
    drivers[i] += tmp
    tmp -= 1

maxScore = max(drivers)
for i in range(len(drivers) - 1):
    if drivers[i] >= maxScore:
        answer += 1
    tmp += 1
    drivers[i+1] += tmp

if drivers[-1] > maxScore:
    print(answer + 1)
else:
    print(answer)



