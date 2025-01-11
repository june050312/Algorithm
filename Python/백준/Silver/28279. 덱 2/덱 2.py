import sys
from collections import deque
deck = deque()
n = int(sys.stdin.readline().strip())
for _ in range(n):
    command = sys.stdin.readline().strip()
    if len(command) > 1:
        command, num = map(int, command.split())
    command = int(command)
    if command == 1:
        deck.appendleft(num)
    elif command == 2:
        deck.append(num)
    elif command == 3:
        try:
            print(deck.popleft())
        except IndexError:
            print(-1)
    elif command == 4:
        try:
            print(deck.pop())
        except IndexError:
            print(-1)
    elif command == 5:
        print(len(deck))
    elif command == 6:
        if len(deck) == 0:
            print(1)
        else:
            print(0)
    elif command == 7:
        try:
            print(deck[0])
        except IndexError:
            print(-1)
    elif command == 8:
        try:
            print(deck[-1])
        except IndexError:
            print(-1)