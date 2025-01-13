N, M = map(int, input().split())
numbers = list(map(int, input().split()))
tc = [tuple(map(int, input().split())) for _ in range(M)]

prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + numbers[i - 1]

for i, j in tc:
    print(prefix_sum[j] - prefix_sum[i - 1])
