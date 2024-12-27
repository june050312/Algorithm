import sys

a = [-1] * 26
b = 0
for i in list(sys.stdin.readline().rstrip()):
    if a[ord(i)-97] == -1:
        a[ord(i)-97] = b
    b += 1
print(*a)