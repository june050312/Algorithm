def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

import sys
a, b = map(int, sys.stdin.readline().strip().split())
print(gcd(a, b))
print(a * b // gcd(a, b))