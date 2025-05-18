from itertools import combinations

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

players = list(range(n))
min_diff = float('inf')

for team1 in combinations(players, n // 2):
    team2 = [p for p in players if p not in team1]

    a = 0
    b = 0

    for i in range(n // 2):
        for j in range(n // 2):
            a += s[team1[i]][team1[j]]
            b += s[team2[i]][team2[j]]

    diff = abs(a - b)
    if diff == 0:
        print(0)
        exit()
    min_diff = min(min_diff, diff)

print(min_diff)