def solution(land):
    
    N = len(land)
    dp = [[0] * 4 for _ in range(N)]
    
    for n in range(N):
        for c in range(4):
            prev = 0
            for i in range(4):
                if i != c:
                    prev = max(prev, dp[n - 1][i])
                
            dp[n][c] = prev + land[n][c] 
    
    return max(dp[N - 1])