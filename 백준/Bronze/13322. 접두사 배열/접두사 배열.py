import sys

def solve():
    input = sys.stdin.read
    data = input().strip()

    n = len(data)

    result = "\n".join(map(str, range(n)))
    sys.stdout.write(result + "\n")

if __name__ == "__main__":
    solve()