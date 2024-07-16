import sys
input = sys.stdin.read

def solution(words):
    unique_words = list(set(words))
    unique_words.sort(key=lambda word: (len(word), word))
    return unique_words

data = input().split()
words = data[1:]

for word in solution(words):
    print(word)