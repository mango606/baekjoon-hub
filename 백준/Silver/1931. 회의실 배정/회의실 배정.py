n = int(input())  # 회의의 수
meetings = [tuple(map(int, input().split())) for _ in range(n)]  # 회의의 시작시간과 끝나는 시간

meetings.sort(key=lambda x: (x[1], x[0]))

# 첫 번째 회의 선택
last_end_time = meetings[0][1]
count = 1

# 두 번째 회의 확인
for i in range(1, n):
    if meetings[i][0] >= last_end_time:
        count += 1
        last_end_time = meetings[i][1]

print(count)