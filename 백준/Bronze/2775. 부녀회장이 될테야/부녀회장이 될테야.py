def solution(floor, room):
    people = [i for i in range(1, room + 1)]
    
    for _ in range(floor):
        for j in range(1, room):
            people[j] += people[j - 1]

    return people[-1]

t = int(input())

for _ in range(t):
    k = int(input())  # 층 수
    n = int(input())  # 호 수
    print(solution(k, n))