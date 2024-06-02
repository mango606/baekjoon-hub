import sys
input = sys.stdin.read

def is_possible(jars, K, mid):
    count = 0
    for jar in jars:
        count += jar // mid
    return count >= K

def max_liquor(jars, K):
    low, high = 1, max(jars)
    answer = 0

    while low <= high:
        mid = (low + high) // 2
        if is_possible(jars, K, mid):
            answer = mid
            low = mid + 1
        else:
            high = mid - 1

    return answer

data = input().split()
N, K = int(data[0]), int(data[1])
jars = list(map(int, data[2:]))

result = max_liquor(jars, K)
print(result)