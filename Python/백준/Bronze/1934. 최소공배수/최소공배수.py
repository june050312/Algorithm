def gcd(x, y):
    if x < y:
        x, y = y, x
    if y == 0:
        return x
    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)

import sys
n = int(sys.stdin.readline())
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    print(x * y // gcd(x, y))