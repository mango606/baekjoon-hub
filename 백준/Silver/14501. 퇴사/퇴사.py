import sys
input = sys.stdin.read

def max_profit(n, T, P):
    dp = [0] * (n + 2)
    
    for i in range(1, n + 1):
        # 오늘 상담을 수행하지 않는 경우
        dp[i + 1] = max(dp[i + 1], dp[i])
        
        # 오늘 상담을 수행하는 경우
        if i + T[i] <= n + 1:
            dp[i + T[i]] = max(dp[i + T[i]], dp[i] + P[i])

    return max(dp)

data = input().split()
n = int(data[0])
T, P = [0] * (n + 1), [0] * (n + 1)

for i in range(1, n + 1):
    T[i], P[i] = map(int, data[2 * i - 1:2 * i + 1])

result = max_profit(n, T, P)
print(result)