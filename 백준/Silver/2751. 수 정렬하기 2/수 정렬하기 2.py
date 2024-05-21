import sys
input = sys.stdin.read

def sort_numbers(numbers):
    numbers.sort()
    return numbers

data = input().split()
n = int(data[0])
numbers = list(map(int, data[1:]))

sorted_numbers = sort_numbers(numbers)

for number in sorted_numbers:
    print(number)