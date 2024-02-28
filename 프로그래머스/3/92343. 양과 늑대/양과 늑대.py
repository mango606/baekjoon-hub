def solution(info, edges):
    graph = {i: [] for i in range(len(info))}
    for a, b in edges:
        graph[a].append(b)

    # 결과를 저장할 변수
    max_sheep = [0]
    
    # 백트래킹을 사용한 DFS 탐색
    def dfs(node, sheep, wolves, available_nodes, visited):
        if info[node] == 0:
            sheep += 1
        else:
            wolves += 1

        # 양의 수가 늑대의 수보다 많지 않으면 더 이상 탐색하지 않음
        if sheep <= wolves:
            return
        
        # 양의 최대 수를 업데이트
        max_sheep[0] = max(max_sheep[0], sheep)

        # 방문하지 않은 자식 노드를 다음 방문 후보에 추가
        new_available_nodes = available_nodes + graph[node]
        new_visited = visited + [node]
        
        # 가능한 모든 노드에 대해 다음 탐색 시도
        for next_node in new_available_nodes:
            if next_node not in visited:
                dfs(next_node, sheep, wolves, [x for x in new_available_nodes if x != next_node], new_visited)

    # 루트 노드에서 탐색 시작
    dfs(0, 0, 0, [], [])

    return max_sheep[0]