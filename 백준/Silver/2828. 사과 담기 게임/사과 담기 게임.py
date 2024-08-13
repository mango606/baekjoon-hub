import sys

def solution():
    N, M = map(int, sys.stdin.readline().split())
    J = int(sys.stdin.readline())
    now = 1
    answer = 0
    
    for _ in range(J):
        apple = int(sys.stdin.readline())
        
        if now <= apple <= now + (M - 1):
            # 바구니가 사과를 이미 받을 수 있는 경우
            pass
        elif apple < now:
            # 사과가 바구니의 왼쪽에 떨어진 경우
            move_distance = now - apple
            answer += move_distance
            now -= move_distance
        else:
            # 사과가 바구니의 오른쪽에 떨어진 경우
            move_distance = apple - (now + M - 1)
            answer += move_distance
            now += move_distance

    print(answer)

if __name__ == "__main__":
    solution()