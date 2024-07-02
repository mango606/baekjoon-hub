def flip(matrix, x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            matrix[i][j] = 1 - matrix[i][j]

def matrix_equal(A, B, N, M):
    for i in range(N):
        for j in range(M):
            if A[i][j] != B[i][j]:
                return False
    return True

def min_flips_to_equal(A, B, N, M):
    if N < 3 or M < 3:
        return 0 if matrix_equal(A, B, N, M) else -1

    flip_count = 0
    for i in range(N - 2):
        for j in range(M - 2):
            if A[i][j] != B[i][j]:
                flip(A, i, j)
                flip_count += 1

    if matrix_equal(A, B, N, M):
        return flip_count
    else:
        return -1

N, M = map(int, input().split())
A = [list(map(int, list(input().strip()))) for _ in range(N)]
B = [list(map(int, list(input().strip()))) for _ in range(N)]

result = min_flips_to_equal(A, B, N, M)
print(result)