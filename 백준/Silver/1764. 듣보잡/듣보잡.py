n, m = map(int, input().split())
not_heard = set(input() for _ in range(n))  # 듣도 못한 사람의 이름
not_seen = set(input() for _ in range(m))  # 보도 못한 사람의 이름

# 듣도 보도 못한 사람의 명단 구하기
not_heard_seen = sorted(list(not_heard & not_seen))

print(len(not_heard_seen))
for name in not_heard_seen:
    print(name)