N, M = map(int, input().split())
memo = {k: v for k, v in (input().split() for _ in range(N))}
Q = [input() for _ in range(M)]

for q in Q:
    print(memo[q])
