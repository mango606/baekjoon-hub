# 방향: 동, 서, 북, 남
directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

def roll_dice(dice, direction):
    if direction == 0:  # 동쪽
        return [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    elif direction == 1:  # 서쪽
        return [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
    elif direction == 2:  # 북쪽
        return [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
    elif direction == 3:  # 남쪽
        return [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]

n, m, x, y, k = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
commands = list(map(int, input().split()))

dice = [0] * 6

for command in commands:
    direction = command - 1
    nx, ny = x + directions[direction][0], y + directions[direction][1]
    
    # 지도 밖으로 벗어나는 경우
    if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
    
    dice = roll_dice(dice, direction)
    
    # 주사위 바닥과 지도 칸 값 교환
    if board[nx][ny] == 0:
        board[nx][ny] = dice[5]
    else:
        dice[5] = board[nx][ny]
        board[nx][ny] = 0

    print(dice[0])
    
    x, y = nx, ny