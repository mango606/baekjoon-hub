def solution(N, M, snow):
    dp = [[0] * (N + 1) for _ in range(M + 1)]  # 최대 눈덩이 크기
    dp[0][0] = 1  # 눈덩이 크기 1

    for i in range(M):
        for j in range(N):
            if dp[i][j] == 0:
                continue
            if j + 1 <= N:  # 눈덩이를 굴리는 경우
                dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + snow[j])
            if j + 2 <= N:  # 눈덩이를 던지는 경우
                dp[i + 1][j + 2] = max(dp[i + 1][j + 2], (dp[i][j] // 2) + snow[j + 1])

    return max(max(row) for row in dp)

N, M = map(int, input().split())
snow = list(map(int, input().split()))

print(solution(N, M, snow))