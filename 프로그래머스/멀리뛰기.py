def solution(n):
    # 점화식으로 푸는 문제 DP
    answer = 1

    if n < 2:
        return n

    dp = [0 for _ in range(n + 1)]
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        # i를 기준으로 i-1칸에서 1칸 움직일때, i-2칸에서 2칸 움직일때.
        dp[i] = dp[i - 1] + dp[i - 2]

    answer = dp[-1]

    answer %= 1234567

    return answer