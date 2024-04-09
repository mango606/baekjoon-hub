N, K = map(int, input().split())
temperatures = list(map(int, input().split()))

# 초기 윈도우의 온도 합 계산
current_sum = sum(temperatures[:K])
max_sum = current_sum

# 슬라이딩 윈도우를 이용한 연속된 K일간의 온도 합의 최대값 찾기
for i in range(K, N):
    # 현재 윈도우에서 가장 왼쪽에 있는 온도를 빼고, 다음 온도를 더함
    current_sum += temperatures[i] - temperatures[i-K]
    max_sum = max(max_sum, current_sum)

print(max_sum)