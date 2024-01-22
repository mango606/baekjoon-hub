def find_path(graph, N):
    # 플로이드-와샬 알고리즘을 사용하여 각 노드 간의 경로 탐색
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = 1

    return graph

# 입력 받기
N = int(input())  # 정점의 개수
graph = [list(map(int, input().split())) for _ in range(N)]  # 인접 행렬

# 경로 찾기
result = find_path(graph, N)

# 결과 출력
for row in result:
    print(' '.join(map(str, row)))