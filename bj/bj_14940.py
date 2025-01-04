from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

goal = None
result = [[-1] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if grid[i][j] == 2:
            goal = (i, j)
        if grid[i][j] == 0:
            result[i][j] = 0

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

queue = deque([goal])
result[goal[0]][goal[1]] = 0

while queue:
    x, y = queue.popleft()

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1 and result[nx][ny] == -1:
            result[nx][ny] = result[x][y] + 1
            queue.append((nx, ny))

for row in result:
    print(' '.join(map(str, row)))
