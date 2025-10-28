import sys

input = sys.stdin.readline

n, m = map(int, input().split())

friend = [[] for _ in range(n)]
v = [False] * n
ans = False

for _ in range(m):
  f, s = map(int, input().split())
  friend[f].append(s)
  friend[s].append(f)

def dfs(idx, depth):
  global ans
  v[idx] = True

  if depth == 4:
    ans = True
    return
  
  for j in friend[idx]:
    if not v[j]:
      v[j] = True
      dfs(j, depth+1)
      v[j] = False

for i in range(n):
  dfs(i, 0)
  v[i] = False
  if ans:
    print(1)
    break
else:
  print(0)