def count(n):
    dp = [0] * (n+1)

    for i in range(2, n+1):
        # 1을 뺀 경우
        dp[i] = dp[i-1] + 1

        # 2로 나눈 경우
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2] + 1)
        
        # 3으로 나눈 경우
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3] + 1)

    return dp[n]

n = int(input())

print(count(n))
