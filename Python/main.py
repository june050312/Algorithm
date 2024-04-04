import sys

n = int(sys.stdin.readline())

minusBinary = []
while n:
    if n % -2 == 0:
        minusBinary.append(1)
    else:
        minusBinary.append(0)
    n //= -2
print(minusBinary)