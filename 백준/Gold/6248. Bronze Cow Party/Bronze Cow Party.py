import heapq

# 입력 받는 부분을 수정하여 직접 값을 제공합니다.
n, m, x = map(int, input().split())  # 농장 수, 도로 수, 파티가 열리는 농장 번호

# 그래프 초기화
graph = [[] for _ in range(n + 1)]
reverse_graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))  # 정방향 그래프
    graph[b].append((a, c))
    reverse_graph[b].append((a, c))  # 역방향 그래프
    reverse_graph[a].append((b, c))

# 다익스트라 알고리즘 함수
def dijkstra(start, graph):
    distance = [float('inf')] * (n + 1)
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))
    
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        
        for next_node, next_dist in graph[now]:
            cost = dist + next_dist
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(queue, (cost, next_node))
                
    return distance

# 각 농장에서 파티 장소로 가는 최단 경로
distance_to_party = dijkstra(x, reverse_graph)

# 파티 장소에서 각 농장으로 돌아가는 최단 경로
distance_from_party = dijkstra(x, graph)

# 최대 왕복 시간 계산
max_trip_time = max(distance_to_party[i] + distance_from_party[i] for i in range(1, n + 1))

print(max_trip_time)