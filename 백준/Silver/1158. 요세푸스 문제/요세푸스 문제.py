from collections import deque

N, K = map(int, input().split())
people = deque(range(1, N+1))

result = []

while people:
    # K-1번 회전시키고, 제거된 사람을 결과 리스트에 추가
    people.rotate(-K+1)
    result.append(people.popleft())

print("<" + ", ".join(map(str, result)) + ">")