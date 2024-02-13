import sys

# 입력 받기
n = int(sys.stdin.readline().strip())

for _ in range(n):
    s = sys.stdin.readline().strip()
    stack = []
    is_vps = True  # Valid Parenthesis String 여부를 체크하는 변수
    
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                is_vps = False
                break  # 올바르지 않은 괄호 문자열이므로 반복문 탈출
    
    # 반복문 종료 후 스택이 비어있지 않으면 올바르지 않은 괄호 문자열
    if stack:
        is_vps = False
    
    # 결과 출력
    print("YES" if is_vps else "NO")