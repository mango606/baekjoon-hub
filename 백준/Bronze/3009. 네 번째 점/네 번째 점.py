def solution(points):
    x_coords = [p[0] for p in points]
    y_coords = [p[1] for p in points]
    
    # 각 좌표에 대해 개수가 1인 것을 찾음
    for x in x_coords:
        if x_coords.count(x) == 1:
            x_fourth = x
            break

    for y in y_coords:
        if y_coords.count(y) == 1:
            y_fourth = y
            break

    return x_fourth, y_fourth

points = []
for _ in range(3):
    x, y = map(int, input().split())
    points.append((x, y))

x4, y4 = solution(points)
print(x4, y4)