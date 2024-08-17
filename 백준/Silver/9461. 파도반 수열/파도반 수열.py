def find_pado(n):
    if n <= 3:
        return 1
    dp = [0] * (n+1)
    dp[1], dp[2], dp[3] = 1, 1, 1
    for i in range(4, n+1):
        dp[i] = dp[i-2] + dp[i-3]
    return dp[n]

import sys
input = sys.stdin.read

data = input().split()
t = int(data[0])
cases = [int(data[i]) for i in range(1, t+1)]

results = [find_pado(case) for case in cases]
for result in results:
    print(result)