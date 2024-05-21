import sys
input = sys.stdin.read

def max_word_sum(words):
    weight = {}
    # 각 알파벳의 가중치 계산
    for word in words:
        length = len(word)
        for i, char in enumerate(word):
            if char in weight:
                weight[char] += 10 ** (length - i - 1)
            else:
                weight[char] = 10 ** (length - i - 1)

    # 가중치를 기준으로 정렬하고 숫자 할당
    sorted_weight = sorted(weight.items(), key=lambda x: -x[1])
    assign_number = 9
    total_sum = 0
    number_map = {}

    for char, _ in sorted_weight:
        number_map[char] = assign_number
        assign_number -= 1

    # 숫자 할당 결과를 통해 최대 합 계산
    for word in words:
        current_sum = 0
        length = len(word)
        for i, char in enumerate(word):
            current_sum += number_map[char] * 10 ** (length - i - 1)
        total_sum += current_sum

    return total_sum

data = input().split()
n = int(data[0])
words = data[1:]

result = max_word_sum(words)
print(result)