import sys
input = sys.stdin.read

def solution(points):
    points.sort(key=lambda point: (point[1], point[0]))
    return points

data = input().split()
n = int(data[0])
points = []

for i in range(1, len(data), 2):
    x, y = int(data[i]), int(data[i+1])
    points.append((x, y))

sorted_points = solution(points)

for point in sorted_points:
    print(point[0], point[1])