import sys
input = sys.stdin.read

def latest_start_time(tasks, n):
    # 마감 시간에 따라 정렬 (내림차순)
    tasks.sort(reverse=True, key=lambda x: x[1])

    # 역순으로 계산 시작
    max_start_time = tasks[0][1]  # 최초 최대 시작 시간은 첫 번째 일의 마감 시간
    for duration, deadline in tasks:
        # 현재 일을 끝내야 하는 최대 시간을 계산
        latest_finish_time = min(max_start_time, deadline)
        # 일을 시작할 수 있는 최신 시간을 업데이트
        max_start_time = latest_finish_time - duration

    # 모든 일을 수행할 수 있는지 확인
    return max_start_time if max_start_time >= 0 else -1

data = input().split()
n = int(data[0])
tasks = []

for i in range(n):
    T, S = map(int, data[2 * i + 1: 2 * i + 3])
    tasks.append((T, S))

result = latest_start_time(tasks, n)

print(result)