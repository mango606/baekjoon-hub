import sys
input = sys.stdin.read

def coin_combinations(coins, k):
    dp = [0] * (k + 1)
    dp[0] = 1

    for coin in coins:
        for amount in range(coin, k + 1):
            dp[amount] += dp[amount - coin]
    
    return dp[k]

data = input().split()
n = int(data[0])
k = int(data[1])
coins = list(map(int, data[2:]))

result = coin_combinations(coins, k)
print(result)