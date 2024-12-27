import sys
stack = []
result, p = 0, 0
for i in list(sys.stdin.readline().rstrip()):
    if i == '(':
        stack.append(i)
        p = 0
    else:
        stack.pop()
        if p == 0:
            result += len(stack)
            p = 1
        else:
            result += 1
print(result)