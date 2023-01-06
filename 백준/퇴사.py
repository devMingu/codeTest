n = int(input())
consultant = [[]]

dp = [0 for _ in range(n+2)]

for _ in range(n):
    T, P = map(int, input().split())
    consultant.append([T, P])

answer = 0
for day in range(n, 0, -1):
    time = consultant[day][0] - 1
    pay = consultant[day][1]

    if day + time > n:
        dp[day] = dp[day + 1]
    else:
        dp[day] = max(dp[day+1], pay + dp[day + time + 1])

print(dp[1])



