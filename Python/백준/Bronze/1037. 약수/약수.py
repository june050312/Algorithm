import sys

input = sys.stdin.readline

amt = int(input())
realAqt = list(map(int, input().split()))

if amt == 1:
    print(realAqt[0] ** 2)
else:
    print(min(realAqt) * max(realAqt))