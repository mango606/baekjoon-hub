from collections import deque
import sys
input = sys.stdin.read

data = input().split()
m, n = int(data[0]), int(data[1])
grid = []
index = 2
for i in range(n):
    grid.append(list(map(int, data[index:index+m])))
    index += m

queue = deque()
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            queue.append((i, j, 0))  # (행, 열, 날짜)

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
max_days = 0

while queue:
    x, y, days = queue.popleft()
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0:
            grid[nx][ny] = 1
            queue.append((nx, ny, days + 1))
            max_days = max(max_days, days + 1)

for row in grid:
    if 0 in row:
        print(-1)
        break
else:
    print(max_days)