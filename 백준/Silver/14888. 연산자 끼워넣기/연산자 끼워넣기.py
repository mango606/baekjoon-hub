import sys
input = sys.stdin.read

def calculate_max_min(numbers, operators, current_result, index, max_result, min_result):
    if index == len(numbers):
        return max(max_result, current_result), min(min_result, current_result)
    
    next_number = numbers[index]
    results = []

    if operators[0] > 0:
        operators[0] -= 1
        results.append(calculate_max_min(numbers, operators, current_result + next_number, index + 1, max_result, min_result))
        operators[0] += 1
    if operators[1] > 0:
        operators[1] -= 1
        results.append(calculate_max_min(numbers, operators, current_result - next_number, index + 1, max_result, min_result))
        operators[1] += 1
    if operators[2] > 0:
        operators[2] -= 1
        results.append(calculate_max_min(numbers, operators, current_result * next_number, index + 1, max_result, min_result))
        operators[2] += 1
    if operators[3] > 0:
        operators[3] -= 1
        if current_result < 0 and next_number > 0:
            results.append(calculate_max_min(numbers, operators, -(abs(current_result) // next_number), index + 1, max_result, min_result))
        else:
            results.append(calculate_max_min(numbers, operators, current_result // next_number, index + 1, max_result, min_result))
        operators[3] += 1
    
    for result in results:
        max_result = max(max_result, result[0])
        min_result = min(min_result, result[1])
    
    return max_result, min_result

data = input().split()
n = int(data[0])
numbers = list(map(int, data[1:n+1]))
operators = list(map(int, data[n+1:n+5]))

initial_result = numbers[0]
max_result, min_result = calculate_max_min(numbers, operators, initial_result, 1, float('-inf'), float('inf'))

print(max_result)
print(min_result)