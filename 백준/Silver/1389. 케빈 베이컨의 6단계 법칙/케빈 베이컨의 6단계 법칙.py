# 입력 받기
N, M = map(int, input().split())  # 유저의 수 N, 친구 관계의 수 M
INF = float('inf')
graph = [[INF] * (N + 1) for _ in range(N + 1)]

# 자기 자신으로의 거리는 0으로 초기화
for i in range(1, N + 1):
    graph[i][i] = 0

# 친구 관계 입력 받아 그래프 구성
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 플로이드-와샬 알고리즘 실행
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 케빈 베이컨 수 계산 및 최솟값을 가진 사람 찾기
min_value = INF
person = 0
for i in range(1, N + 1):
    temp = sum(graph[i][1:N+1])
    if temp < min_value:
        min_value = temp
        person = i

# 결과 출력
print(person)