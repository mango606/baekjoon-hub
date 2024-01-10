# 주어진 블루레이 크기로 모든 강의를 M개 이하의 블루레이에 담을 수 있는지 확인하는 함수
def record(size, lectures, M):
    count, sum = 0, 0
    for lecture in lectures:
        if lecture > size:
            return False
        if sum + lecture > size:
            count += 1
            sum = lecture
        else:
            sum += lecture
    if sum > 0:
        count += 1
    return count <= M

# 이진 탐색을 사용하여 필요한 최소 블루레이 크기를 찾는 함수
def min_size(N, M, lectures):
    low, high = max(lectures), sum(lectures)
    result = high

    while low <= high:
        mid = (low + high) // 2
        if record(mid, lectures, M):
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return result

N, M = map(int, input().split())  # 강의의 수 N, 블루레이의 수 M
lectures = list(map(int, input().split()))  # 강의의 길이
print(min_size(N, M, lectures))