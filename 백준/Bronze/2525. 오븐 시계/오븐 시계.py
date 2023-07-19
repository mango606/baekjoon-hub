a, b = map(int, input().split())
c = int(input())

b = b + c
while b > 59 :
    b -= 60
    a += 1
    
    if (a > 23) : a -= 24

print(a, b)