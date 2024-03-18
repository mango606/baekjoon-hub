n = int(input())  # 사람의 수
times = list(map(int, input().split()))  # 각 사람이 돈을 인출하는데 필요한 시간

# 오름차순 정렬
times.sort()

total = 0
for i in range(n):
    total += times[i] * (n-i)

print(total)