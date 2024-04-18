max_value = -1  # 초기화
max_row = 0     # 행 위치
max_col = 0     # 열 위치

for i in range(9):
    row = list(map(int, input().split()))
    for j in range(9):
        if row[j] > max_value:
            max_value = row[j]
            max_row = i + 1
            max_col = j + 1

print(max_value)
print(max_row, max_col)