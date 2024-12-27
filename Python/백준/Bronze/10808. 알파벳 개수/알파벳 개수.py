import sys

a = [0] * 26
for i in list(sys.stdin.readline().rstrip()):
    a[ord(i)-97] += 1
print(*a)