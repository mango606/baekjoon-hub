t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    for i in range (1, b+1):
        if (a*i % b == 0):
            print(a*i)
            break