import sys
input = sys.stdin.read

def find_common_pattern(filenames):
    n = len(filenames)
    length = len(filenames[0])
    pattern = list(filenames[0])  # 첫 번째 파일명을 패턴으로 초기화

    for i in range(1, n):  # 첫 번째 파일명을 제외한 나머지 파일명을 순회
        for j in range(length):
            if pattern[j] != filenames[i][j]:  # 현재 위치의 문자가 다르면 '?'로 변경
                pattern[j] = '?'

    return ''.join(pattern)  # 리스트를 문자열로 변환하여 반환

data = input().split()
n = int(data[0])
filenames = data[1:]
result = find_common_pattern(filenames)
print(result)