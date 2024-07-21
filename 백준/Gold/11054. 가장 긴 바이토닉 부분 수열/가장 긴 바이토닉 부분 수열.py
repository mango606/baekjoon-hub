import sys
input = sys.stdin.read

def solution(arr):
    n = len(arr)
    lis = [1] * n
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                lis[i] = max(lis[i], lis[j] + 1)
    
    lds = [1] * n
    for i in range(n-1, -1, -1):
        for j in range(n-1, i, -1):
            if arr[j] < arr[i]:
                lds[i] = max(lds[i], lds[j] + 1)

    max_length = 0
    for i in range(n):
        max_length = max(max_length, lis[i] + lds[i] - 1)

    return max_length

data = input().split()
n = int(data[0])
arr = list(map(int, data[1:]))

result = solution(arr)

print(result)