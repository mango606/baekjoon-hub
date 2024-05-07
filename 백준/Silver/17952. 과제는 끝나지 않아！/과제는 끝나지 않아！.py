import sys
input = sys.stdin.readline

# (점수, 남은 시간)을 저장하는 스택
tasks = []
total_score = 0
n = int(input().strip())

for _ in range(n):
    input_data = list(map(int, input().split()))

    if input_data[0] == 1:
        # 새로운 과제가 주어진 경우
        score, time_required = input_data[1], input_data[2]
        tasks.append([score, time_required])

    # 현재 처리 중인 과제가 있는 경우
    if tasks:
        tasks[-1][1] -= 1  # 1분 처리
        # 남은 시간이 0이면 과제를 완료
        if tasks[-1][1] == 0:
            total_score += tasks.pop()[0]

print(total_score)