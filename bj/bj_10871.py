N, X = map(int, input().split())
A = list(map(int, input().split()))

filtered = []
for i in range(N):
    if A[i] < X:
        filtered.append(A[i])

print(*filtered)
