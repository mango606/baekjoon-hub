def count_stars(N):
    from math import factorial
    if N < 5:
        return 0
    return factorial(N) // (factorial(5) * factorial(N - 5))

if __name__ == "__main__":
    N = int(input())
    print(count_stars(N))