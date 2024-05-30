import sys
input = sys.stdin.read

def can_cut_trees(trees, M, H):
    total = sum((tree - H) for tree in trees if tree > H)
    return total >= M

def find_max_height(trees, M):
    low, high = 0, max(trees)
    answer = 0

    while low <= high:
        mid = (low + high) // 2
        if can_cut_trees(trees, M, mid):
            answer = mid
            low = mid + 1
        else:
            high = mid - 1

    return answer

data = input().split()
N, M = int(data[0]), int(data[1])
trees = list(map(int, data[2:]))

result = find_max_height(trees, M)
print(result)