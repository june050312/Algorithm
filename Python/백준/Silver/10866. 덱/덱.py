import sys
from collections import deque
n = int(sys.stdin.readline())
dq = deque()
for _ in range(n):
    cmd = sys.stdin.readline().strip()
    if 'push' in cmd:
        cmd, num = map(str, cmd.split())
        if cmd == 'push_front':
            dq.appendleft(int(num))
        elif cmd == 'push_back':
            dq.append(int(num))
    elif 'pop' in cmd:
        if cmd == 'pop_front':
            try:
                print(dq.popleft())
            except IndexError:
                print(-1)
        elif cmd == 'pop_back':
            try:
                print(dq.pop())
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