import sys
from collections import deque
n = int(sys.stdin.readline())
stack = deque()
result = deque()
temp = 1
check = 0
for _ in range(n):
    num = int(sys.stdin.readline())
    while num >= temp:
        stack.append(temp)
        result.append('+')
        temp += 1
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        check = 1
        break
if check == 0:
    for i in result:
        print(i)