def find_fraction(x):
    line = 1  # 지그재그 대각선 번호
    while x > line:
        x -= line  # 대각선의 원소 개수를 차감하면서 x를 줄여나감
        line += 1

    # x번째 분수는 line 번째 대각선에 위치
    # line이 짝수일 때는 분자가 증가하는 방향, 홀수일 때는 분모가 증가하는 방향으로 움직임
    if line % 2 == 0:
        numerator = x   # 분자
        denominator = line - x + 1  # 분모
    else:
        numerator = line - x + 1
        denominator = x

    return f"{numerator}/{denominator}"

if __name__ == "__main__":
    X = int(input())
    result = find_fraction(X)
    print(result)