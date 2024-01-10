def can_record(blue_ray_size, lectures, M):
    count, temp_sum = 0, 0
    for lecture in lectures:
        if lecture > blue_ray_size:
            return False
        if temp_sum + lecture > blue_ray_size:
            count += 1
            temp_sum = lecture
        else:
            temp_sum += lecture
    if temp_sum > 0:
        count += 1
    return count <= M

def min_blue_ray_size(N, M, lectures):
    low, high = max(lectures), sum(lectures)
    result = high

    while low <= high:
        mid = (low + high) // 2
        if can_record(mid, lectures, M):
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return result

# 입력 받기
N, M = map(int, input().split())  # 강의의 수 N, 블루레이의 수 M
lectures = list(map(int, input().split()))  # 강의들의 길이

# 결과 출력
print(min_blue_ray_size(N, M, lectures))