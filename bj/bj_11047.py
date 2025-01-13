N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]

count = 0
won = 0
for a in reversed(A):
    while won + a <= K:
        won += a
        count += 1

print(count)
