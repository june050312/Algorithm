import sys

input = sys.stdin.readline

# 1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19
E, S, M = map(int, input().split())

ans = 1
e = 1
s = 1
m = 1
while 1:
    if e == E and s == S and m == M:
        print(ans)
        break

    e += 1
    if e > 15:
        e = 1
    s += 1
    if s > 28:
        s = 1
    m += 1
    if m > 19:
        m = 1
    ans += 1