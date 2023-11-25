def solution(num, n):
    answer = num % n
    
    if answer == 0:
        return 1
    else: return 0