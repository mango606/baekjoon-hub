from sys import stdin, stdout
import collections

input = stdin.read
data = input().split()
n = int(data[0])  # 노드 수
m = int(data[1])  # 간선 수
v = int(data[2])  # 시작 노드

graph = collections.defaultdict(list)
index = 3
for _ in range(m):
    x, y = int(data[index]), int(data[index+1])
    graph[x].append(y)
    graph[y].append(x)
    index += 2

for key in graph:
    graph[key].sort()

# DFS
def dfs(v, visited=[]):
    visited.append(v)
    for neighbor in graph[v]:
        if neighbor not in visited:
            dfs(neighbor, visited)
    return visited

# BFS
def bfs(v):
    visited = []
    queue = collections.deque([v])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend([n for n in graph[node] if n not in visited])
    return visited

dfs_result = dfs(v)
bfs_result = bfs(v)
stdout.write(' '.join(map(str, dfs_result)) + '\n')
stdout.write(' '.join(map(str, bfs_result)) + '\n')