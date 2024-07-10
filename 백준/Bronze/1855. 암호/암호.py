from sys import stdin

n = int(stdin.readline())
s = stdin.readline().rstrip()
arr = [list(s[i:i+n]) if i % (2*n) == 0 else list(s[i:i+n][::-1]) for i in range(0, len(s), n)]
res = ''.join(''.join(arr[j][i] for j in range(len(arr))) for i in range(n))
print(res)