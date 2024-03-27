i = j = k = sum = 0
dp = [[False for col in range(10)] for row in range(1001)]

for i in range(0, 10):
    dp[1][i] = 1
    
for j in range (2, 1001):
    for i in range (10):
        for k in range(i+1):
            dp[j][i] += dp[j - 1][k] % 10007

n = int(input())

for i in range(0, 10):
    sum += dp[n][i]

print(sum % 10007)