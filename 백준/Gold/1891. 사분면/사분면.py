import sys

def solution():
    d, num = sys.stdin.readline().rstrip().split()
    d = int(d)
    num = list(num)
    a, b = map(int, sys.stdin.readline().split())

    x, y = 0, 0
    n = d

    for i in num:
        i = int(i)
        n -= 1
        size = 2 ** n

        if i == 1:  # 1사분면
            y += size
        elif i == 2:  # 2사분면
            pass
        elif i == 3:  # 3사분면
            x += size
        elif i == 4:  # 4사분면
            x += size
            y += size

    x -= b
    y += a

    if x < 0 or x >= 2 ** d or y < 0 or y >= 2 ** d:
        print(-1)
        return

    answer = ""
    for i in range(d):
        size = 2 ** (d - i - 1)
        if x < size and y < size:  # 2사분면
            answer += "2"
        elif x < size and y >= size:  # 1사분면
            answer += "1"
            y -= size
        elif x >= size and y < size:  # 3사분면
            answer += "3"
            x -= size
        elif x >= size and y >= size:  # 4사분면
            answer += "4"
            x -= size
            y -= size

    print(answer)

if __name__ == "__main__":
    solution()