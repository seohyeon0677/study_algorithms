N = int(input())
grid = [tuple(map(int, input().split())) for _ in range(N)]

grid.sort(key=lambda x: (x[1], x[0]))

for x in grid:
    print(x[0], x[1])
