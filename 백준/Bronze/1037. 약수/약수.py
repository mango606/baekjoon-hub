n = int(input())
measure = list(map(int, input().split()))
print(max(measure) * min(measure))