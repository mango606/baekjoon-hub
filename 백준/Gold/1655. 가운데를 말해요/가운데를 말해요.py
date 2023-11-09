import heapq
import sys

# 입력을 빠르게 받기 위한 설정
input = sys.stdin.readline

# 백준이가 외치는 정수의 개수 N을 입력받음
N = int(input())

# 최대 힙과 최소 힙 초기화
max_heap = []  # 왼쪽 그룹 (작은 수들)
min_heap = []  # 오른쪽 그룹 (큰 수들)

for _ in range(N):
    num = int(input())

    # 최대 힙의 크기와 최소 힙의 크기를 동일하게 유지하거나, 최대 힙이 1 더 크게 유지
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, (-num, num))
    else:
        heapq.heappush(min_heap, (num, num))

    # 최대 힙의 루트가 최소 힙의 루트보다 클 경우 두 힙의 루트를 교환
    if min_heap and max_heap[0][1] > min_heap[0][0]:
        max_val = heapq.heappop(max_heap)[1]
        min_val = heapq.heappop(min_heap)[0]
        heapq.heappush(max_heap, (-min_val, min_val))
        heapq.heappush(min_heap, (max_val, max_val))

    # 현재 중간값 출력
    print(max_heap[0][1])