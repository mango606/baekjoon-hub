import sys
import heapq

input = sys.stdin.read

data = input().strip().split()
n = int(data[0])
lectures = []

for i in range(n):
    start, end = int(data[2 * i + 1]), int(data[2 * i + 2])
    lectures.append((start, end))

lectures.sort()

min_heap = []

for start, end in lectures:
    if min_heap and min_heap[0] <= start:
        heapq.heappop(min_heap)
    heapq.heappush(min_heap, end)

print(len(min_heap))