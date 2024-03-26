t = int(input())  # 테스트 케이스 개수

zero_count = [1, 0]
one_count = [0, 1]

for i in range(2, 41):
    zero_count.append(zero_count[i-1] + zero_count[i-2])
    one_count.append(one_count[i-1] + one_count[i-2])

for _ in range(t):
    n = int(input())  # 호출되는 n 값
    print(zero_count[n], one_count[n])