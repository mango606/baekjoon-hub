n = int(input())  # 수열의 크기
numbers = list(map(int, input().split()))  # 수열
x = int(input())  # 목표 합 X

numbers.sort()

count = 0  # X와 같아지는 경우의 수
left, right = 0, n-1

while left < right:
    current_sum = numbers[left] + numbers[right]
    if current_sum == x:  # 합이 X와 같으면
        count += 1
        left += 1
        right -= 1
    elif current_sum < x:  # 합이 X보다 작으면
        left += 1
    else:  # 합이 X보다 크면
        right -= 1

print(count)