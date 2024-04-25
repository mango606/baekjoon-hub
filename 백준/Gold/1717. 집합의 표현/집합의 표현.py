import sys
input = sys.stdin.read

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)
    if rootA != rootB:
        parent[rootB] = rootA

def solve():
    input_data = input().split()
    index = 0
    n = int(input_data[index])
    index += 1
    m = int(input_data[index])
    index += 1
    
    parent = list(range(n + 1))
    result = []

    for _ in range(m):
        operation = int(input_data[index])
        index += 1
        a = int(input_data[index])
        index += 1
        b = int(input_data[index])
        index += 1
        
        if operation == 0:
            union(parent, a, b)
        elif operation == 1:
            if find(parent, a) == find(parent, b):
                result.append("YES")
            else:
                result.append("NO")

    print("\n".join(result))

if __name__ == "__main__":
    solve()