import sys

input = sys.stdin.readline

h, w = map(int, input().split())
ans = min(h, w) * 2 - 1
if w >= h:
    ans -= 1
print(ans)