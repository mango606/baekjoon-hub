import math

a, b = map(int, input().split())
result = b * math.log10(a) + 1  # 로그 규칙에 따른 연산

print(int(result + 1e-9))  # 실수 오차 보정