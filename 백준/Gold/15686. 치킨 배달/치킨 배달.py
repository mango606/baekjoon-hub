from itertools import combinations
import sys

input = sys.stdin.read

def calculate_chicken_distance(houses, chickens, m):
    chicken_combinations = combinations(chickens, m)
    min_city_chicken_distance = float('inf')
    
    for chicken_set in chicken_combinations:
        city_chicken_distance = 0
        for hx, hy in houses:
            chicken_distance = min(abs(hx - cx) + abs(hy - cy) for cx, cy in chicken_set)
            city_chicken_distance += chicken_distance
        min_city_chicken_distance = min(min_city_chicken_distance, city_chicken_distance)
    
    return min_city_chicken_distance

def main():
    data = input().split()
    n, m = int(data[0]), int(data[1])
    grid = []
    index = 2
    houses = []
    chickens = []
    
    for i in range(n):
        row = data[index:index + n]
        grid.append(row)
        for j in range(n):
            if row[j] == '1':
                houses.append((i, j))
            elif row[j] == '2':
                chickens.append((i, j))
        index += n

    result = calculate_chicken_distance(houses, chickens, m)
    print(result)

main()