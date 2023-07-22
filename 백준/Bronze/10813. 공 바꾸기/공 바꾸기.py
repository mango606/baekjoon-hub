n, m = map(int, input().split())
basket = [0] * n

# n개의 바구니에는 바구니에 적혀있는 번호와 같은 번호가 적힌 공이 들어있음.
for i in range(0, n):
    basket[i] = i+1

# m번 공을 바꿈.
for _ in range(m):
    i, j = map(int, input().split())
    temp = basket[i-1]
    basket[i-1] = basket[j-1]
    basket[j-1] = temp

for i in range(0, n):
    print(basket[i], end = ' ')