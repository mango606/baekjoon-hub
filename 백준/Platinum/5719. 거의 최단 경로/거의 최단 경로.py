import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    distance = [INF] * (n + 1)
    distance[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))
    
    while pq:
        dist, now = heapq.heappop(pq)
        if distance[now] < dist:
            continue
        
        for next_node, weight in graph[now]:
            if weight == -1:  # 제거된 간선은 무시
                continue
            cost = dist + weight
            if cost < distance[next_node]:
                distance[next_node] = cost
                way[next_node] = [now]
                heapq.heappush(pq, (cost, next_node))
            elif cost == distance[next_node]:
                way[next_node].append(now)
                
    return distance

def bfs(end):
    q = [end]
    while q:
        now = q.pop(0)
        if check[now]:
            continue
        check[now] = True
        for prev in way[now]:
            for i, (next_node, _) in enumerate(graph[prev]):
                if next_node == now:
                    graph[prev][i] = (next_node, -1)  # 간선 삭제
            q.append(prev)

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    start, end = map(int, input().split())
    
    graph = [[] for _ in range(n + 1)]
    way = [[] for _ in range(n + 1)]
    check = [False] * (n + 1)
    
    for _ in range(m):
        u, v, e = map(int, input().split())
        graph[u].append((v, e))
    
    dijkstra(start)
    bfs(end)
    
    distance = dijkstra(start)
    print(distance[end] if distance[end] != INF else -1)