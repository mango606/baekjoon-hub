strings = [input() for _ in range(5)]

# 가장 긴 문자열의 길이 찾기
max_length = max(len(s) for s in strings)

# 세로로 읽기
for i in range(max_length):
    for s in strings:
        if i < len(s):
            print(s[i], end='')