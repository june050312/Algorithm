def gcd(x, y):
    if y > x:
        x, y = y, x
    while y:
        x, y = y, x % y
    return x

import sys

n, s = map(int, sys.stdin.readline().strip().split())
a = list(map(int, sys.stdin.readline().strip().split()))

d = []
for i in a:
    d.append(abs(s - i))

result = d[0]
for i in range(1, n):
    result = gcd(d[i], result)
print(result)