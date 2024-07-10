import itertools

n = int(input())
senior_promises = [input().split() for _ in range(n)]
senior_funds = {name: int(amount) for name, amount in (input().split() for _ in range(n))}

meal_days = [False] * 80

for senior, week, day, cost in senior_promises:
    week, day, cost = map(int, [week, day, cost])
    if cost <= senior_funds[senior]:
        meal_days[week * 7 + day] = True

max_continuous_meals = max((sum(1 for _ in group) for is_meal, group in itertools.groupby(meal_days) if is_meal), default=0)
print(max_continuous_meals)