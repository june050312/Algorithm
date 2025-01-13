import sys

input = sys.stdin.readline

n = int(input())
m = list(map(int, input().split()))

ans = []
i = 0
while 1:
    if m[i+1] > m[i]:
        j = i + 1
        while j + 1 <= len(m) - 1 and m[j+1] > m[j] :
            j += 1
        ans.append(m[j] - m[i])
        i = j
    i += 1
    if len(m) - 1 <= i:
        break
        
try:        
    print(max(ans))
except:
    print(0)