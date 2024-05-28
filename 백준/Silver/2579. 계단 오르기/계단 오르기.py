import sys
input = sys.stdin.read

def max_score(stairs, n):
    if n == 1:
        return stairs[1]
    elif n == 2:
        return stairs[1] + stairs[2]
    elif n == 3:
        return max(stairs[1] + stairs[3], stairs[2] + stairs[3])

    dp = [0] * (n + 1)
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]
    dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

    for i in range(4, n + 1):
        dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])

    return dp[n]

data = sys.stdin.read().strip().split()
n = int(data[0])
stairs = [0] * (n + 1)

for i in range(1, n + 1):
    stairs[i] = int(data[i])

result = max_score(stairs, n)
print(result)