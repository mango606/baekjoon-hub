def pizza(n):
    if n == 1:
        return 0
    else:
        return (n-1) + pizza(n-1)

n = int(input())
print(pizza(n))