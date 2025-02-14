def solution(phone_number):
    hide_length = len(phone_number) - 4
    answer = '*' * hide_length + phone_number[-4:]
    return answer