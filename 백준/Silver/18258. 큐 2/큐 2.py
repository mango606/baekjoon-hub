import sys
from collections import deque
input = sys.stdin.read

def process_commands(commands):
    queue = deque()
    result = []

    for command in commands:
        parts = command.split()
        cmd = parts[0]

        if cmd == "push":
            queue.append(parts[1])
        elif cmd == "pop":
            result.append(queue.popleft() if queue else "-1")
        elif cmd == "size":
            result.append(str(len(queue)))
        elif cmd == "empty":
            result.append("0" if queue else "1")
        elif cmd == "front":
            result.append(queue[0] if queue else "-1")
        elif cmd == "back":
            result.append(queue[-1] if queue else "-1")
    
    return '\n'.join(result)

commands = sys.stdin.read().strip().split('\n')[1:]
result = process_commands(commands)
print(result)