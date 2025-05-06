s = input()
answer = set()

for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        answer.add(s[i:j])

print(len(answer))