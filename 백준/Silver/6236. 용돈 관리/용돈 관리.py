import sys
input = sys.stdin.read

def can_withdraw(days, M, K):
    current_sum = 0
    count = 1
    
    for cost in days:
        if current_sum + cost > K:
            count += 1
            current_sum = cost
            if count > M:
                return False
        else:
            current_sum += cost

    return True

def find_min_K(days, M):
    low, high = max(days), sum(days)
    result = high

    while low <= high:
        mid = (low + high) // 2
        if can_withdraw(days, M, mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return result

data = input().split()
N, M = int(data[0]), int(data[1])
days = list(map(int, data[2:]))

result = find_min_K(days, M)
print(result)