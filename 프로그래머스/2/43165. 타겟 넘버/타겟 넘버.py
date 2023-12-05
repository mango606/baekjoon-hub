def dfs(numbers, target, depth, sum):
    if depth == len(numbers):
        return sum == target
        
    return dfs(numbers, target, depth+1, sum+numbers[depth]) + dfs(numbers, target, depth+1, sum-numbers[depth])

def solution(numbers, target):
    return dfs(numbers, target, 0, 0)