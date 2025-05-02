import sys

input = sys.stdin.readline

def dfs(start):
    if (len(s) == r):
        print(' '.join(map(str, s)))
        return
    
    for i in range(start, n + 1):
        s.append(i)
        dfs(i)
        s.pop()

n, r = map(int, input().split())
s = []

dfs(1)