# 방향 벡터 (상, 하, 좌, 우)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def simulate_bomb_explosion(grid, r, c):
    new_grid = [['O'] * c for _ in range(r)]
    
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 'O':
                new_grid[i][j] = '.'
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < r and 0 <= nj < c:
                        new_grid[ni][nj] = '.'
    return new_grid

def solve():
    r, c, n = map(int, input().split())
    grid = [list(input().strip()) for _ in range(r)]

    if n == 1:
        # 주어진 상태 그대로 출력
        for row in grid:
            print(''.join(row))
    elif n % 2 == 0:
        # 모든 칸에 폭탄이 가득 찬 상태 출력
        for _ in range(r):
            print('O' * c)
    else:
        # 폭탄이 한 번 또는 두 번 폭발한 후의 상태
        grid_first = simulate_bomb_explosion(grid, r, c)
        grid_second = simulate_bomb_explosion(grid_first, r, c)

        if n % 4 == 3:
            # 첫 번째 폭발 후의 상태
            for row in grid_first:
                print(''.join(row))
        else:
            # 두 번째 폭발 후의 상태
            for row in grid_second:
                print(''.join(row))

if __name__ == "__main__":
    solve()