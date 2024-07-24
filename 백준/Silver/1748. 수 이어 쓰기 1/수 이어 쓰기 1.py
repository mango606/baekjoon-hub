import sys
input = sys.stdin.read

n = int(input().strip())
length = 0
current_length = len(str(n))
for i in range(current_length - 1):
    num_of_numbers = 9 * (10 ** i)
    length += num_of_numbers * (i + 1)
length += (n - 10**(current_length - 1) + 1) * current_length

print(length)