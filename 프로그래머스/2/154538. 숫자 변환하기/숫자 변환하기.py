from collections import deque

def solution(x, y, n):
    queue = deque([(x, 0)])
    visited = set()
    visited.add(x)
    
    while queue:
        current, steps = queue.popleft()
        
        if current == y:
            return steps
        
        operations = [current + n, current * 2, current * 3]
        
        for next_value in operations:
            if next_value > y or next_value in visited:
                continue
            visited.add(next_value)
            queue.append((next_value, steps + 1))
    
    return -1