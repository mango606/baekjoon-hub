import sys
input = sys.stdin.read

def number_of_nodes(n):
    return 2 ** n

n = int(input().strip())

result = number_of_nodes(n)

print(result)