import sys

input = sys.stdin.readline

n = int(input())

ans = 0
for i in range(1, n + 1):
    ans += (n // i) * i
    
print(ans)