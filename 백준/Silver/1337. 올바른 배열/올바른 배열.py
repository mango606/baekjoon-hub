n = int(input())  # 수열의 크기
numbers = sorted(int(input()) for _ in range(n))

min_needed = 4  # 최대 4개 필요

for i in range(n):
    # i에서 시작하는 연속하는 5개의 숫자 중 순차적인 최대 개수 찾기
    count = 1
    for j in range(i+1, min(i+5, n)):
        if numbers[j] - numbers[i] <= 4:
            count += 1
    min_needed = min(min_needed, 5 - count)

print(min_needed)