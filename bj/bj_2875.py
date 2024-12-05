F, M, K = map(int, input().split())

team = 0
f = F
m = M

for _ in range(M):
    f -= 2
    m -= 1
    if f + m < K:
        break
    if f < 0 or m < 0:
        break
    team += 1

print(team)
