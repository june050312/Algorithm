import sys

input = sys.stdin.readline

num = int(input())
ans = ""

if not num:
    ans += "0"
else:
    while num:
        if num % -2:
            ans += "1"
            num = num // -2 + 1
        else:
            ans += "0"
            num //= -2

print(ans[::-1])