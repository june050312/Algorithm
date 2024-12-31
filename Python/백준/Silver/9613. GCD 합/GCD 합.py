def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

import sys


for i in range(int(sys.stdin.readline().strip())):
    result = 0
    numList = list(map(int, sys.stdin.readline().strip().split()))
    t = numList[0]
    for j in range(1, t):
        for k in range(j + 1, t + 1):
            result += gcd(numList[j], numList[k])
    print(result)