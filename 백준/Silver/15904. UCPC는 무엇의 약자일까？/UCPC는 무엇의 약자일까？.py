def solution(sentence):
    target = "UCPC"
    idx = 0
    for char in sentence:
        if char == target[idx]:
            idx += 1
            if idx == len(target):
                return "I love UCPC"
    return "I hate UCPC"

import sys
input = sys.stdin.read
sentence = input().strip()
print(solution(sentence))