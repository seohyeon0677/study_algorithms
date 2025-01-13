def solve():
    T = int(input())
    tc = [int(input()) for _ in range(T)]

    max_n = max(tc)
    dp = [0] * (max_n + 1)
    dp[1], dp[2], dp[3] = 1, 2, 4

    for i in range(4, max_n + 1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
    for n in tc:
        print(dp[n])

solve()
