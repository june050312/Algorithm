import sys
from collections import deque
n = int(sys.stdin.readline())
for _ in range(n):
    word = deque(sys.stdin.readline().strip().split())
    for i in word:
        print(i[::-1], end = ' ')
    print()