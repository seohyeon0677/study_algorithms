N = int(input())
M = [tuple(map(int, input().split())) for _ in range(N)]

ranks = [1] * N

for i in range(N):
    for j in range(N):
        if i != j:
            if M[i][0] < M[j][0] and M[i][1] < M [j][1]:
                ranks[i] += 1

print(" ".join(map(str, ranks)))
