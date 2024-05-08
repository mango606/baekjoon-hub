n, k = map(int, input().split())
initial = list(map(int, input().split()))
d = list(map(int, input().split()))

d = [x - 1 for x in d]

def solution(arr, d):
    new_arr = [0] * len(arr)
    for i, idx in enumerate(d):
        new_arr[idx] = arr[i]
    return new_arr

current = initial[:]
for _ in range(k):
    current = solution(current, d)

print(' '.join(map(str, current)))