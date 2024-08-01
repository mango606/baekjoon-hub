import sys
input = sys.stdin.read

def generate_sequences(arr, sequence, used, M):
    if len(sequence) == M:
        print(' '.join(map(str, sequence)))
        return
    
    for i in range(len(arr)):
        if not used[i]:
            used[i] = True
            sequence.append(arr[i])
            generate_sequences(arr, sequence, used, M)
            sequence.pop()
            used[i] = False

def main():
    data = input().split()
    N = int(data[0])
    M = int(data[1])
    arr = list(map(int, data[2:]))

    arr.sort()
    used = [False] * N
    generate_sequences(arr, [], used, M)

main()