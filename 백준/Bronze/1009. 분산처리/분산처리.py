T = int(input())  # 테스트 케이스의 수

for _ in range(T):
    a, b = map(int, input().split())
    a %= 10

    if a == 0:
        print(10)
        continue

    cycle = [a]
    while True:
        next_num = (cycle[-1] * a) % 10
        if next_num == cycle[0]:
            break
        cycle.append(next_num)

    print(cycle[(b % len(cycle)) - 1])