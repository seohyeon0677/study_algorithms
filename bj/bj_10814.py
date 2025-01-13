N = int(input())
P = [tuple(input().split()) for _ in range(N)]
members = [(int(P[i][0]), P[i][1], i) for i in range(N)]

members.sort(key=lambda x: (x[0], x[2]))

for age, name, _ in members:
    print(age, name)
