import sys
arr1 = list(sys.stdin.readline().strip())
arr2 = []
n = int(sys.stdin.readline())
for _ in range(n):
    cmd = sys.stdin.readline().strip()
    if cmd == 'L':
        if arr1:
            arr2.append(arr1.pop())
    elif cmd == 'D':
        if arr2:
            arr1.append(arr2.pop())
    elif cmd == 'B':
        if arr1:
            arr1.pop()
    else:
        cmd, word = cmd.split()
        arr1.append(word)
arr1.extend(reversed(arr2))
print(''.join(arr1))