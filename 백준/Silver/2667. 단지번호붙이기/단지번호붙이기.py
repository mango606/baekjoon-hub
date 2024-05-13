from collections import deque
import sys
input = sys.stdin.read

def bfs(start_x, start_y):
    queue = deque([(start_x, start_y)])
    grid[start_x][start_y] = '0'  # 방문한 곳을 0으로 표시
    count = 1
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == '1':
                grid[nx][ny] = '0'
                queue.append((nx, ny))
                count += 1
    return count

data = input().split()
n = int(data[0])
grid = [list(data[i + 1]) for i in range(n)]

# 각 단지별 집의 수 저장
house_counts = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == '1':
            house_counts.append(bfs(i, j))

house_counts.sort()
print(len(house_counts))
for count in house_counts:
    print(count)