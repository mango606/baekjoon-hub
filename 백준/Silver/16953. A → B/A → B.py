def min_operations(A, B):
    operations = 0
    while B > A:
        if B % 10 == 1:
            B = (B - 1) // 10
        elif B % 2 == 0:
            B //= 2
        else:
            return -1
        operations += 1
    
    if B < A:
        return -1
    
    return operations + 1

import sys
input = sys.stdin.read
A, B = map(int, input().split())

result = min_operations(A, B)

print(result)