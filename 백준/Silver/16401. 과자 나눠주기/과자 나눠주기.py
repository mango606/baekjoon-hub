def can_allocate(m, snacks, H):
    count = 0
    for snack in snacks:
        count += snack // H
    return count >= m

def max_snack_length(m, snacks):
    low, high = 1, max(snacks)
    result = 0

    while low <= high:
        mid = (low + high) // 2
        if can_allocate(m, snacks, mid):
            result = mid
            low = mid + 1
        else:
            high = mid - 1

    return result

# 입력 받기
M, N = map(int, input().split())  # 조카의 수 M, 과자의 수 N
snacks = list(map(int, input().split()))  # 과자의 길이들

# 결과 출력
print(max_snack_length(M, snacks))