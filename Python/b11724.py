import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(cur):
    visited[cur] = 1

    for next in adj[cur]:
        if not visited[next]:
            dfs(next)

n, m = map(int, input().split())

adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

cnt = 0
visited = [0] * (n + 1)
while visited.count(0) > 1:
    dfs(visited.index(0, 1))
    cnt += 1

print(cnt)