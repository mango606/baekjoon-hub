import heapq

def dijkstra(start, end, N, roads):
    graph = [[] for _ in range(N + 1)]
    for a, b, cost in roads:
        graph[a].append((b, cost))

    distances = [float('inf')] * (N + 1)
    paths = [[] for _ in range(N + 1)]

    distances[start] = 0
    paths[start] = [start]
    queue = [(0, start)]

    while queue:
        current_distance, current = heapq.heappop(queue)

        if distances[current] < current_distance:
            continue

        for next_node, next_distance in graph[current]:
            distance = current_distance + next_distance

            if distance < distances[next_node]:
                distances[next_node] = distance
                paths[next_node] = paths[current] + [next_node]
                heapq.heappush(queue, (distance, next_node))

    return distances[end], paths[end]

# 입력 받기
N = int(input())  # 도시의 수
M = int(input())  # 버스의 수
roads = [list(map(int, input().split())) for _ in range(M)]
start, end = map(int, input().split())

# 다익스트라 알고리즘 실행
min_cost, path = dijkstra(start, end, N, roads)

# 결과 출력
print(min_cost)
print(len(path))
print(' '.join(map(str, path)))