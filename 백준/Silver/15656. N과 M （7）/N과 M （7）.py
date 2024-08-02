import sys
input = sys.stdin.read

def generate_sequences(arr, sequence, M):
    if len(sequence) == M:
        print(' '.join(map(str, sequence)))
        return
    
    for i in range(len(arr)):
        sequence.append(arr[i])
        generate_sequences(arr, sequence, M)
        sequence.pop()

def main():
    data = input().split()
    N = int(data[0])
    M = int(data[1])
    arr = list(map(int, data[2:]))

    arr.sort()
    generate_sequences(arr, [], M)

main()