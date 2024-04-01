def calculate_min_turns(N, wheel, M, target):
    wheel += wheel  # 돌림판을 이어붙여서 반시계 방향 회전을 간단히 처리
    pos = N - 1  # 처음에 마지막 문자를 가리키고 시작
    total_turns = 0

    for char in target:
        next_pos = wheel.find(char, pos + 1)  # 현재 위치 이후에 문자를 찾음
        if next_pos == -1:
            return -1  # 문자를 찾을 수 없으면 -1 반환
        turn = next_pos - pos
        total_turns += turn
        pos = next_pos % N  # 다음 문자 위치 업데이트 (원형 구조를 유지)

    return total_turns

N = int(input())
wheel = input()
M = int(input())
target = input()

print(calculate_min_turns(N, wheel, M, target))