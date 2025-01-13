def isPrime(x):
    if x == 1:
        return False
    else:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True

import sys
from collections import deque
minimum = int(sys.stdin.readline().strip())
maximum = int(sys.stdin.readline().strip())
primeList = deque()
for i in range(minimum, maximum + 1):
    if isPrime(i):
        primeList.append(i)
if not primeList:
    print(-1)
else:
    print(sum(primeList))
    print(min(primeList))