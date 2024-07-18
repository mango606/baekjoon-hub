import sys

def classify_triangle(angles):
    if sum(angles) != 180:
        return "Error"
    unique_angles = len(set(angles))
    if unique_angles == 1 and angles[0] == 60:
        return "Equilateral"
    elif unique_angles == 2:
        return "Isosceles"
    elif unique_angles == 3:
        return "Scalene"

angles = []
for _ in range(3):
    angle = int(sys.stdin.readline().strip())
    angles.append(angle)

result = classify_triangle(angles)
print(result)