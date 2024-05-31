import sys
input = sys.stdin.read

def can_make_cables(cables, length, N):
    total = sum(cable // length for cable in cables)
    return total >= N

def find_max_length(cables, N):
    low, high = 1, max(cables)
    result = 0

    while low <= high:
        mid = (low + high) // 2
        if can_make_cables(cables, mid, N):
            result = mid
            low = mid + 1
        else:
            high = mid - 1

    return result

data = input().split()
K, N = int(data[0]), int(data[1])
cables = [int(data[i]) for i in range(2, 2 + K)]

result = find_max_length(cables, N)
print(result)