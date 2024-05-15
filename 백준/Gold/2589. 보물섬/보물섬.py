from collections import deque
import sys
input = sys.stdin.read

def bfs(x, y, grid):
    n, m = len(grid), len(grid[0])
    visited = [[-1] * m for _ in range(n)]
    queue = deque([(x, y)])
    visited[x][y] = 0
    max_dist = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 'L' and visited[nx][ny] == -1:
                visited[nx][ny] = visited[cx][cy] + 1
                max_dist = max(max_dist, visited[nx][ny])
                queue.append((nx, ny))
    return max_dist

def find_longest_path(grid):
    n, m = len(grid), len(grid[0])
    max_distance = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'L':
                max_distance = max(max_distance, bfs(i, j, grid))
    return max_distance

data = input().split()
n, m = int(data[0]), int(data[1])
grid = [list(data[i + 2].strip()) for i in range(n)]

result = find_longest_path(grid)
print(result)