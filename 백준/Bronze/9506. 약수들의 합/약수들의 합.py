def solution(n):
    if n < 2:
        return False, []
    
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    
    if sum(divisors) == n:
        return True, divisors
    else:
        return False, []

while True:
    n = int(input())
    if n == -1:
        break
    
    is_perfect, divisors =  solution(n)
    if is_perfect:
        print(f"{n} = " + " + ".join(map(str, divisors)))
    else:
        print(f"{n} is NOT perfect.")