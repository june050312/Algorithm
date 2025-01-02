import sys
input = sys.stdin.readline

n = int(input())
m = list(map(int, input().strip().split()))
stack = []

c = 1
for _ in range(len(m)):
    if m[0] == c:
        m.pop(0)
        c += 1
        for __ in range(len(stack)):
            if stack[-1] == c:
                stack.pop(-1)
                c += 1
    else:
        stack.append(m.pop(0))

if not m and not stack:
    print("Nice")
else:
    print("Sad")