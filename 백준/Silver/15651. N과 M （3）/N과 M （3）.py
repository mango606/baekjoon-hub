N, M = map(int, input().split())

output = []

def dfs(depth):
    if depth == M:
        print(' '.join(map(str, output)))
        return
    for i in range(1, N+1):
        output.append(i)
        dfs(depth + 1)
        output.pop()

dfs(0)