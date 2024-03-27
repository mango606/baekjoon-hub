def solution(m, n, puddles):
    graph = [[0]*n for _ in range(m)]

    for a in range(len(graph[0])):
        if [1,a+1] not in puddles:
            graph[0][a] = 1
        else:
            break
    for b in range(len(graph)):
        if [b+1,1] not in puddles: 
            graph[b][0] = 1
        else:
            break


    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if i==0 or j==0:
                continue
            if [i+1,j+1] in puddles:
                continue
            else:
                graph[i][j] = graph[i-1][j] + graph[i][j-1]
    return graph[m-1][n-1]%1000000007

solution(4, 3, [2,2])