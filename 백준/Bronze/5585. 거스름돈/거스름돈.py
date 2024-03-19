n = int(input())
n = 1000 - n
cnt = 0

while True:
    if n >= 500:
        n -= 500
        cnt += 1
    elif n >= 100:
        n -= 100
        cnt += 1
    elif n >= 50:
        n -= 50
        cnt += 1
    elif n >= 10:
        n -= 10
        cnt += 1
    elif n >= 5:
        n -= 5
        cnt += 1
    elif n >= 1:
        n -= 1
        cnt += 1
    else:
        print(cnt)
        break