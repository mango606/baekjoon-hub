from collections import deque

N, K = map(int, input().split())
queue = deque(range(1, N+1))

answer = []

while queue:
    queue.rotate(-(K-1))  # K번째 사람을 제거하기 위해 K-1번 회전
    answer.append(queue.popleft())  # 회전 후 맨 앞의 사람을 제거

print("<" + ", ".join(map(str, answer)) + ">")