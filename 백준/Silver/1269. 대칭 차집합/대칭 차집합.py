import sys
input = sys.stdin.read

def symmetrical_difference_size(a, b):
    set_a = set(a)
    set_b = set(b)
    return len(set_a.symmetric_difference(set_b))

data = input().split()
n, m = int(data[0]), int(data[1])
a = map(int, data[2:2+n])
b = map(int, data[2+n:])

result = symmetrical_difference_size(a, b)

print(result)