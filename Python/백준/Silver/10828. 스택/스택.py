import sys
from collections import deque
amount = int(sys.stdin.readline())
stack = []
for _ in range(amount):
    command = sys.stdin.readline().strip()
    if 'push' in command:
        command, num = map(str, command.split())
    if command == 'push':
        stack.append(int(num))
    elif command == 'pop':
        try:
            print(stack.pop())
        except IndexError:
            print(-1)
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
    elif command == 'top':
        try:    
            print(stack[-1])
        except IndexError:
            print(-1)