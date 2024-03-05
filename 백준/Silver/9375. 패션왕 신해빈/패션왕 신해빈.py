t = int(input())  # 테스트 케이스의 수

for _ in range(t):
    n = int(input())  # 의상의 수
    clothes = {}  # 의상 종류별로 의상의 수를 저장할 딕셔너리

    for _ in range(n):
        _, category = input().split()
        if category in clothes:
            clothes[category] += 1
        else:
            clothes[category] = 1

    result = 1
    for count in clothes.values():
        result *= (count + 1)  # 각 종류별로 의상을 입거나 입지 않는 경우의 수

    print(result - 1)