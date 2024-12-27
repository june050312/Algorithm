import sys
from collections import deque
n, gap = map(int, sys.stdin.readline().split())
people = deque(range(1, n + 1))
popList = deque()
while True:
    if not people:
        break
    people.rotate(-(gap - 1))
    popList.append(people.popleft())
print('<', end = '')
for i in range(len(popList) - 1):
    print(popList[i], end = ', ')
print(popList[-1], '>', sep = '')