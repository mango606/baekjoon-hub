import sys
import math

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

input = sys.stdin.read
data = input().split()
n = int(data[0])
numbers = map(int, data[1:])
count = sum(1 for num in numbers if is_prime(num))

print(count)