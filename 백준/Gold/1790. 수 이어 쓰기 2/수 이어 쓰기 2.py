def solution(N, k):
    digit_length = 0
    num_count = 9
    current_digit = 1
    
    while k > num_count * current_digit:
        k -= num_count * current_digit
        digit_length += num_count * current_digit
        num_count *= 10
        current_digit += 1
    
    if k > (N - 10**(current_digit-1) + 1) * current_digit:
        return -1
    
    start_number = 10**(current_digit-1)
    number = start_number + (k-1) // current_digit
    
    if number > N:
        return -1

    return int(str(number)[(k-1) % current_digit])

N, k = map(int, input().split())
print(solution(N, k))