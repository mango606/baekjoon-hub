from collections import Counter

def create_palindrome(s):
    count = Counter(s)
    odd_count = sum(1 for x in count.values() if x % 2 != 0)

    if odd_count > 1:
        return "I'm Sorry Hansoo"

    middle = ''
    first_half = []
    for char in sorted(count.keys()):
        if count[char] % 2 != 0:
            middle = char
        first_half.append(char * (count[char] // 2))

    first_half = ''.join(first_half)
    palindrome = first_half + middle + first_half[::-1]
    return palindrome

s = input().strip()

result = create_palindrome(s)
print(result)