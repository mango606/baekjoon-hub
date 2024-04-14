n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]
numbers.sort()

left, right = 0, 1
min_diff = float('inf')

while right < n:
    current_diff = numbers[right] - numbers[left]

    if current_diff >= m:
        min_diff = min(min_diff, current_diff)
        if left + 1 < right:
            left += 1
        else:
            right += 1
            left += 1
    else:
        right += 1

print(min_diff)