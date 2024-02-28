from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n + 1)]
parents = [0] * (n + 1)

# 트리 구성을 위한 연결 정보 입력 받기
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# BFS를 사용하여 각 노드의 부모 찾기
def bfs():
    queue = deque([1])
    while queue:
        node = queue.popleft()
        for child in tree[node]:
            if parents[child] == 0:
                parents[child] = node
                queue.append(child)

bfs()

for i in range(2, n + 1):
    print(parents[i])