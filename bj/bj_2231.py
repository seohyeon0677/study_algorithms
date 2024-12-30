def sol(N):
    start = max(1, N - 9 * len(str(N)))
    for n in range(start, N):
        n_sum = n + sum(map(int, str(n)))
        if n_sum == N:
            return n
    return 0

N = int(input())

print(sol(N))
