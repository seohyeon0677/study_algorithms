# (몸무게 x, 키 y)
N = int(input())
M = [list(map(int, input().split())) for _ in range(N)]

answer = [N] * N
for a in range(0, N-1):
    for b in range(a+1, N):
        if a != b:
            if M[a][0] > M[b][0] and M[a][1] > M[b][1]:
                answer[a] -= 1
            elif M[a][0] > M[b][0] and M[a][1] > M[b][1]:
                answer[b] -= 1
            else:
                continue

rank = [0] * N
n = 1
while n <= N:
    for m in range(1, N+1):
        count = 0
        for i in range(N):
            if answer[i] == m:
                count += 1
                rank[i] = n
        n += count

print(*rank)