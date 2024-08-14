import sys

N, K = map(int, sys.stdin.readline().split())
dp = [0] * (N + 1)

for _ in range(K):
    I, T = map(int, sys.stdin.readline().split())
    
    for j in range(N, T - 1, -1):
        dp[j] = max(dp[j], dp[j - T] + I)

print(dp[N])