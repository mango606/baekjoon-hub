import sys

# 입력 받기
n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    command = sys.stdin.readline().split()
    
    # 명령 1: 스택에 X 추가
    if command[0] == '1':
        stack.append(int(command[1]))
    # 명령 2: 스택에서 정수 제거 및 출력
    elif command[0] == '2':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    # 명령 3: 스택에 있는 정수의 개수 출력
    elif command[0] == '3':
        print(len(stack))
    # 명령 4: 스택이 비어있는지 확인
    elif command[0] == '4':
        print(1 if not stack else 0)
    # 명령 5: 스택의 맨 위 정수 출력
    elif command[0] == '5':
        if stack:
            print(stack[-1])
        else:
            print(-1)