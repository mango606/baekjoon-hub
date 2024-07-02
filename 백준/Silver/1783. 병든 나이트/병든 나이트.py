def max_cells_visited(N, M):
    if N == 1:
        return 1
    elif N == 2:
        return min(4, (M + 1) // 2)
    elif M < 7:
        return min(4, M)
    else:
        return M - 2

import sys
input = sys.stdin.read
N, M = map(int, input().split())

result = max_cells_visited(N, M)
print(result)