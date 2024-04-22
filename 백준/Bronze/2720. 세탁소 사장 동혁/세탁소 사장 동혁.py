t = int(input())
coins = [25, 10, 5, 1]

for _ in range(t):
    cents = int(input())
    result = []

    for coin in coins:
        count = cents // coin
        result.append(str(count))
        cents %= coin

    print(' '.join(result))