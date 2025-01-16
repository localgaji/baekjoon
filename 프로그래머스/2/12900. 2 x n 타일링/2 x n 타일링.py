def solution(N):
    dp = [0] * (N + 1)
    dp[0], dp[1] = 1, 1

    for n in range(2, N + 1):
        dp[n] = dp[n - 1] + dp[n - 2]
        dp[n] = dp[n] % 1000000007
    return dp[N] 
