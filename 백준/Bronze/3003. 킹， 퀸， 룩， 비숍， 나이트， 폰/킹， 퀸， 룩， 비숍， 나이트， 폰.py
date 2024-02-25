standard = [1, 1, 2, 2, 2, 8]

current = list(map(int, input().split()))

needed = [s - c for s, c in zip(standard, current)]
print(*needed)
