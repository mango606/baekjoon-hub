import sys
import bisect

input = sys.stdin.read
data = input().split()

index = 0
T = int(data[index])
index += 1
results = []

for _ in range(T):
    N = int(data[index])
    M = int(data[index + 1])
    index += 2
    A = list(map(int, data[index:index + N]))
    B = list(map(int, data[index + N:index + N + M]))
    index += N + M

    B.sort()
    count = 0

    for a in A:
        pos = bisect.bisect_left(B, a)
        count += pos

    results.append(str(count))

print("\n".join(results))