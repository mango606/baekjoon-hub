import sys
print(''.join(sorted(sys.stdin.read().strip(), reverse=True)))