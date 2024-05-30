import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = deque((map(int, input().split())))
ballonNum = deque(range(1, n+1))
result = []

for i in range(n):
    c = m.popleft()
    result.append(ballonNum.popleft())
    if c > 0:
        m.rotate(-(c - 1))
        ballonNum.rotate(-(c - 1))
    else:
        m.rotate(-c)
        ballonNum.rotate(-c)

print(*result)