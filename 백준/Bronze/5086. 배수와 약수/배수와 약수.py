import sys
input = sys.stdin.read

def solve():
    input_data = input().split()
    results = []
    i = 0
    while True:
        a = int(input_data[i])
        i += 1
        b = int(input_data[i])
        i += 1
        
        if a == 0 and b == 0:
            break
        
        if b % a == 0:
            results.append("factor")
        elif a % b == 0:
            results.append("multiple")
        else:
            results.append("neither")
    
    print("\n".join(results))

if __name__ == "__main__":
    solve()