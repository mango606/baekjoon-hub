import sys
input = sys.stdin.read

def select_candidates(candidates):
    candidates.sort()
    max_interview_rank = float('inf')
    count = 0

    for _, interview in candidates:
        if interview < max_interview_rank:
            count += 1
            max_interview_rank = interview

    return count

# 입력 처리
data = input().split()
t = int(data[0])  # 테스트 케이스의 수
index = 1

results = []
for _ in range(t):
    n = int(data[index])  # 지원자의 수
    index += 1
    candidates = []
    for _ in range(n):
        paper, interview = map(int, data[index:index+2])
        candidates.append((paper, interview))
        index += 2
    result = select_candidates(candidates)
    results.append(result)

for result in results:
    print(result)