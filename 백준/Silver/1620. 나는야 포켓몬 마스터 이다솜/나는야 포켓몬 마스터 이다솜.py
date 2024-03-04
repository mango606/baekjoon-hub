import sys

n, m = map(int, input().split())
name_to_num = {}  # 이름 키, 번호 값
num_to_name = {}  # 번호 키, 이름 값

for i in range(1, n+1):
    name = sys.stdin.readline().rstrip()
    name_to_num[name] = i
    num_to_name[i] = name

for _ in range(m):
    query = sys.stdin.readline().rstrip()
    if query.isdigit():  # 번호
        print(num_to_name[int(query)])
    else:  # 이름
        print(name_to_num[query])