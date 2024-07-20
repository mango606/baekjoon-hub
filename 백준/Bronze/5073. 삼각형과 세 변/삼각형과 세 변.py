import sys
input = sys.stdin.read

def triangle_type(a, b, c):
    x, y, z = sorted([a, b, c])

    if x + y <= z:
        return "Invalid"

    if x == y == z:
        return "Equilateral"
    elif x == y or y == z or x == z:
        return "Isosceles"
    else:
        return "Scalene"

results = []
for line in sys.stdin.read().strip().split("\n"):
    a, b, c = map(int, line.split())
    if a == 0 and b == 0 and c == 0:
        break
    results.append(triangle_type(a, b, c))

for result in results:
    print(result)