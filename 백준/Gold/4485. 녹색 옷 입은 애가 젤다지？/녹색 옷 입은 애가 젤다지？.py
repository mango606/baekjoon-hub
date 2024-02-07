import sys
import heapq

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
INF = float("inf")
count = 1

while True:
    n = int(input())

    if n == 0:
        break

    cave = [list(map(int, input().split())) for _ in range(n)]
    lost = []  # 잃은 돈
    heapq.heappush(lost, (cave[0][0], 0, 0))
    
    # 최소의 금액을 잃음
    answer = [[INF for _ in range(n)] for _ in range(n)]
    answer[0][0] = cave[0][0]
    result = 0
    
    while lost:
        money, a, b = heapq.heappop(lost)

        # 도착지점에 최소값 저장
        if a == n-1 and b == n-1:
            result = money

        # 델타 탐색
        for ar in range(4):
            dr = a + dx[ar]
            dc = b + dy[ar]
            if 0 <= dr < n and 0 <= dc < n:
            	# 현재까지의 최소돈 + 다음돈 비교
                if money + cave[dc][dr] < answer[dr][dc]:
                    answer[dr][dc] = money + cave[dc][dr]
                    heapq.heappush(lost, (money + cave[dr][dc], dr, dc))
    print('Problem {}: {}'.format(count, result))
    count += 1