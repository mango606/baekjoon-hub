import sys

input = sys.stdin.readline  # 입력 속도 향상
n = int(input().strip())  # strip()을 사용하여 줄바꿈 문자 제거
stack = []

for _ in range(n):
    command = input().split()
    
    if command[0] == "push":
        stack.append(command[1])
    elif command[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "empty":
        print(0 if stack else 1)
    elif command[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)