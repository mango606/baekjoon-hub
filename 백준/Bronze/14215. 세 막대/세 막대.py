import sys
input = sys.stdin.read

def solution(stick_lengths):
    stick_lengths.sort()
    
    a, b, c = stick_lengths
    
    if a + b > c:
        return a + b + c
    else:
        return a + b + (a + b - 1)

stick_lengths = list(map(int, input().split()))
result = solution(stick_lengths)
print(result)