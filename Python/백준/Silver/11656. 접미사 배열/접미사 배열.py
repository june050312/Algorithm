import sys
a = sys.stdin.readline().strip()
b = []
for i in range(len(a)):
    b.append(a[i:])
for i in sorted(b):
    print(i)