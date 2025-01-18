def fibonacci(n):
    dp_0 = [0] * (n + 1)
    dp_1 = [0] * (n + 1)
    dp_0[0] = 1
    dp_1[0] = 0

    if n > 0:
        dp_0[1] = 0
        dp_1[1] = 1

    for i in range(2, n + 1):
        dp_0[i] = dp_0[i - 1] + dp_0[i - 2]
        dp_1[i] = dp_1[i - 1] + dp_1[i - 2]
    
    return dp_0, dp_1

T = int(input())
tc = [int(input()) for _ in range(T)]

max_n = max(tc)
dp_0, dp_1 = fibonacci(max_n)

for n in tc:
    print(dp_0[n], dp_1[n])
