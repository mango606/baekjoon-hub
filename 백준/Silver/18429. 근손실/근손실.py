def solution(N, K, kits, current_weight=500, day=0):
    if day == N:
        return 1
    
    count = 0
    for i in range(N):
        if kits[i] is not None:  # 사용하지 않은 운동 키트인 경우
            new_weight = current_weight + kits[i] - K
            if new_weight >= 500:  # 중량이 500 이상 유지되는 경우만 탐색
                saved_kit = kits[i]
                kits[i] = None  # 현재 운동 키트를 사용했음을 표시
                count += solution(N, K, kits, new_weight, day+1)
                kits[i] = saved_kit  # 다음 탐색을 위해 운동 키트를 복원
    return count

N, K = map(int, input().split())
kits = list(map(int, input().split()))

print(solution(N, K, kits))