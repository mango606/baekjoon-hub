import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node, weight):
    for next_node, next_weight in tree[node]:
        if distance[next_node] == -1:  # 아직 방문하지 않은 노드인 경우
            distance[next_node] = weight + next_weight
            dfs(next_node, weight + next_weight)

V = int(input())
tree = [[] for _ in range(V + 1)]

for _ in range(V):
    info = list(map(int, input().split()))
    node = info[0]
    for i in range(1, len(info) - 2, 2):
        tree[node].append((info[i], info[i + 1]))

distance = [-1] * (V + 1)
distance[1] = 0
dfs(1, 0)

# 가장 먼 노드 찾기
farthest_node = distance.index(max(distance))

distance = [-1] * (V + 1)
distance[farthest_node] = 0
dfs(farthest_node, 0)

print(max(distance))