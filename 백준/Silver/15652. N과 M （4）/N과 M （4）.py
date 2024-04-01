N, M = map(int, input().split())

output = []

def dfs(start):
    if len(output) == M:
        print(' '.join(map(str, output)))
        return
    for i in range(start, N+1):
        output.append(i)
        dfs(i)
        output.pop()

dfs(1)