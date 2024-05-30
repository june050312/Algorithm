import sys
input = sys.stdin.readline

def bfs(init):
    q = []

    q.append(init)
    visited[init] = 1

    while q:
        cur = q.pop(0)

        if cur == end:
            return visited[end]

        for next in family[cur]:
            if not visited[next]:
                q.append(next)
                visited[next] = visited[cur] + 1

n = int(input())
start, end = map(int, input().strip().split())
m = int(input())
family = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().strip().split())
    family[x].append(y)
    family[y].append(x)

for i in range(m):
    family[i].sort()

visited = [0] * (n + 1)
kin = bfs(start)
if kin:
    print(kin - 1)
else:
    print(-1)