n = int(input())
score = list(int(input()) for _ in range(n))

def upstairs(n, score):
    if n == 1:
        return score[0]
    
    dp = [0] * n
    dp[0] = score[0]
    dp[1] = score[0] + score[1]

    for i in range(2, n):
        dp[i] = max(dp[i-2], dp[i-3] + score[i-1]) + score[i]

    return dp[n-1]

print(upstairs(n, score))
