from collections import deque
import sys
input = sys.stdin.read

def bfs(x, y, color, grid, visited):
    queue = deque([(x, y)])
    visited[x][y] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid) and not visited[nx][ny]:
                if grid[nx][ny] == color:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

def count_regions(grid):
    n = len(grid)
    visited = [[False] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j, grid[i][j], grid, visited)
                count += 1
    return count

data = input().split()
n = int(data[0])
grid = [list(data[i + 1].strip()) for i in range(n)]
color_weakness_grid = [row[:] for row in grid]

for i in range(n):
    for j in range(n):
        if color_weakness_grid[i][j] == 'G':
            color_weakness_grid[i][j] = 'R'

normal_count = count_regions(grid)
color_weakness_count = count_regions(color_weakness_grid)

print(normal_count, color_weakness_count)