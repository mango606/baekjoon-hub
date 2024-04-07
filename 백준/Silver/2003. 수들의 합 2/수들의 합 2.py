def solution(n, m, arr):
    count = 0
    for start in range(n):
        sum_ = 0
        for end in range(start, n):
            sum_ += arr[end]
            if sum_ == m:
                count += 1
                break
            elif sum_ > m:
                break
    return count

n, m = map(int, input().split())
arr = list(map(int, input().split()))

print(solution(n, m, arr))