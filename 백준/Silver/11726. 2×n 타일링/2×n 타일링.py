import sys
input = sys.stdin.read

def count_tiling_ways(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 10007
    
    return dp[n]

n = int(input())

print(count_tiling_ways(n))