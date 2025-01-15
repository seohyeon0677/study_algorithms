N = int(input())
P = list(map(int, input().split()))

P.sort()

time = [0] * N
time[0] = P[0]
for i in range(1, N):
    time[i] = time[i-1] + P[i]

print(sum(time))
