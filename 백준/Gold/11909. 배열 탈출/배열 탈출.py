import sys

def escape_array(n, heights):
    dp = [[float('inf') for _ in range(n)] for _ in range(n)]
    dp[0][0] = 0  # 시작점의 비용은 0

    for i in range(n):
        for j in range(n):
            if i > 0:
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + max(0, heights[i][j] - heights[i - 1][j] + 1))
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j - 1] + max(0, heights[i][j] - heights[i][j - 1] + 1))

    return dp[n - 1][n - 1]

input = sys.stdin.readline
n = int(input())
heights = [list(map(int, input().split())) for _ in range(n)]

print(escape_array(n, heights))