N, M = map(int, input().split())

visited = [False] * (N + 1)  # 방문 여부
output = []  # 수열 출력

def dfs(depth):
    if depth == M:
        print(' '.join(map(str, output)))
        return
    for i in range(1, N+1):
        if not visited[i]:  # 아직 방문하지 않은 경우
            visited[i] = True
            output.append(i)
            dfs(depth + 1)
            visited[i] = False
            output.pop()

dfs(0)