import sys
input = sys.stdin.readline

def dfs(cur):
    visited[cur] = 1

    for next in network[cur]:
        if not visited[next]:
            dfs(next)

n = int(input().strip())
m = int(input().strip())

network = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e = map(int, input().strip().split())
    network[s].append(e)
    network[e].append(s)

for i in range(1, n + 1):
    network[i].sort()

visited = [0] * (n + 1)
dfs(1)
print(visited.count(1) - 1)