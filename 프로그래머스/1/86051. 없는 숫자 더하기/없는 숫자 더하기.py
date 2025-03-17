def solution(numbers):
    all_numbers = set(range(10))
    numbers_set = set(numbers)
    missing_numbers = all_numbers - numbers_set
    answer = sum(missing_numbers)
    return answer