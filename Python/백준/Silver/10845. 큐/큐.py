import sys
from collections import deque
n = int(sys.stdin.readline())
dq = deque()
for _ in range(n):
    cmd = sys.stdin.readline().strip()
    if 'push' in cmd:
        cmd, num = map(str, cmd.split())
        dq.append(int(num))
    elif cmd == 'pop':
        try:
            print(dq.popleft())
        except IndexError:
            print(-1)
    elif cmd == 'size':
        print(len(dq))
    elif cmd == 'empty':
        if not dq:
            print(1)
        else:
            print(0)
    elif cmd == 'front':
        try:
            print(dq[0])
        except IndexError:
            print(-1)
    elif cmd == 'back':
        try:
            print(dq[-1])
        except IndexError:
            print(-1)
