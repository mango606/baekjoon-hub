from collections import deque

def bfs(grid, N, M):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    queue = deque()
    visited = [[False for _ in range(M)] for _ in range(N)]

    # 상어가 있는 위치를 찾아 큐에 넣고, 방문 처리한다
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:
                queue.append((i, j, 0))
                visited[i][j] = True

    max_distance = 0

    while queue:
        x, y, distance = queue.popleft()
        max_distance = max(max_distance, distance)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, distance + 1))

    return max_distance

# 입력 받기
N, M = map(int, input().split())  # 맵의 크기
grid = [list(map(int, input().split())) for _ in range(N)]

# BFS 실행 및 결과 출력
print(bfs(grid, N, M))