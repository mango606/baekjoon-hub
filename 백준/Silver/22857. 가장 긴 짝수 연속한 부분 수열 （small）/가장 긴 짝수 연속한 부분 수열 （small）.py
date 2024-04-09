n, k = map(int, input().split())
numbers = list(map(int, input().split()))

max_length = 0  # 가장 긴 짝수 부분수열의 길이
odd_count = 0  # 홀수 개수
left = 0

for right in range(n):
    # 현재 숫자가 홀수인 경우
    if numbers[right] % 2 != 0:
        odd_count += 1
    
    # 홀수의 개수가 K 초과
    while odd_count > k:
        if numbers[left] % 2 != 0:
            odd_count -= 1
        left += 1
    
    max_length = max(max_length, right - left + 1 - odd_count)

print(max_length)