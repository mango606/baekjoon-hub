from itertools import combinations
from copy import deepcopy
from collections import deque

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(virus_map):
    queue = deque()
    # 초기 바이러스 위치를 큐에 추가
    for i in range(n):
        for j in range(m):
            if virus_map[i][j] == 2:
                queue.append((i, j))
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and virus_map[nx][ny] == 0:
                virus_map[nx][ny] = 2
                queue.append((nx, ny))
    
    # 안전 영역 크기 계산
    safe_count = sum(row.count(0) for row in virus_map)
    return safe_count

# 벽을 세울 수 있는 위치 찾기
empty_spaces = [(i, j) for i in range(n) for j in range(m) if lab[i][j] == 0]
max_safe_area = 0

# 모든 가능한 벽 3개의 조합에 대해 시뮬레이션
for walls in combinations(empty_spaces, 3):
    test_lab = deepcopy(lab)
    # 벽 세우기
    for x, y in walls:
        test_lab[x][y] = 1
    # 바이러스 퍼뜨리기 및 안전 영역 계산
    max_safe_area = max(max_safe_area, bfs(test_lab))

print(max_safe_area)