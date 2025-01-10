def isPrime(x):
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

import sys
n = int(sys.stdin.readline())
for _ in range(n):
    num = int(sys.stdin.readline())
    while True:
        if num == 0 or num == 1:
            print(2)
            break
        if isPrime(num):
            print(num)
            break
        num += 1