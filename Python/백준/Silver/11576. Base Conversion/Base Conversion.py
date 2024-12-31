import sys

input = sys.stdin.readline

A, B = map(int, input().split())
m = int(input())
t = list(map(int, input().split()))

decimal = 0
for index, i in enumerate(t[::-1]):
    decimal += i * A ** index

ans = []
if not decimal:
    print(0)
    exit()
while decimal:
    if decimal % B:
        ans.append(decimal % B)
    else:
        ans.append(0)
    decimal //= B

print(*ans[::-1])