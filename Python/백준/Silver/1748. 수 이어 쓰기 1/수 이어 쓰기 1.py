import sys

input = sys.stdin.readline

n = int(input())

cnt = 0
numLen = len(str(n))
for i in range(numLen - 1):
    cnt += ((10 ** (i + 1)) - (10 ** i)) * (i + 1)
cnt += (n - (10 ** (numLen - 1) - 1)) * numLen
print(cnt)