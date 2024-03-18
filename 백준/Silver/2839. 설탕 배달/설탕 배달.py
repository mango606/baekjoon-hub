n = int(input())

bags = 0

while n >= 0:
    if n % 5 == 0:  # 5로 나누어 떨어지면
        bags += n // 5
        print(bags)
        break
    n -= 3  # 5kg 봉지로 나누어 떨어지지 않으면
    bags += 1
else:
    print(-1)  # 정확하게 나눌 수 없으면 -1을 출력합니다.
