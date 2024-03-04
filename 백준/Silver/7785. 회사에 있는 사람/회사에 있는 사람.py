n = int(input())  # 로그 기록의 수
people_in_company = set()  # 회사에 있는 사람들을 저장할 집합

for _ in range(n):
    name, status = input().split()
    if status == 'enter':
        people_in_company.add(name)
    elif status == 'leave':
        people_in_company.discard(name)

for name in sorted(people_in_company, reverse=True):
    print(name)