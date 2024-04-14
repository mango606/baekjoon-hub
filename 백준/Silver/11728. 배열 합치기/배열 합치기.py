import sys
input = sys.stdin.read

def solution(A, B):
    i, j = 0, 0
    merged = []
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            merged.append(A[i])
            i += 1
        else:
            merged.append(B[j])
            j += 1
    merged.extend(A[i:])
    merged.extend(B[j:])
    return merged

data = input().split()
n = int(data[0])
m = int(data[1])
A = list(map(int, data[2:2+n]))
B = list(map(int, data[2+n:2+n+m]))

result = solution(A, B)
print(' '.join(map(str, result)))