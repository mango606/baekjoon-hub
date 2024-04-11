n = int(input())
group_word_count = 0

for _ in range(n):
    word = input()
    seen = set()
    is_group_word = True
    prev_char = ''

    for char in word:
        if char in seen and char != prev_char:
            is_group_word = False
            break
        seen.add(char)
        prev_char = char

    if is_group_word:
        group_word_count += 1

print(group_word_count)