def working(N, work):
    dp = [0] * (N + 1)

    for i in range(N - 1, -1, -1):
        t, p = work[i]

        if i + t <= N:
            dp[i] = max(dp[i+1], p + dp[i+t])
        else:
            dp[i] = dp[i+1]
    
    return dp[0]

N = int(input())
work = [tuple(map(int, input().split())) for _ in range(N)]

print(working(N, work))
