import sys
input = sys.stdin.read
from bisect import bisect_left, bisect_right
    
data = input().split()
N = int(data[0])
M = int(data[1])
    
points = sorted(map(int, data[2:N+2]))
segments = [(int(data[2+N+2*i]), int(data[2+N+2*i+1])) for i in range(M)]
    
results = []
    
for start, end in segments:
    left_index = bisect_left(points, start)
    right_index = bisect_right(points, end)
    results.append(right_index - left_index)
    
for result in results:
    print(result)