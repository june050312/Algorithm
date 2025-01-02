import sys
from collections import deque
input = sys.stdin.readline

def bfs(init):
    q = deque()
    cnt = 0

    q.append(init)
    visited[init] = 1

    while q:
        cur = q.popleft()

        for next in trust[cur]:
            if not visited[next]:
                visited[next] = 1
                q.append(next)
                cnt += 1

    return cnt

n, m = map(int, input().split())

trust = [[] for _ in range(n + 1)]
for _ in range(m):
    e, s = map(int, input().split())
    trust[s].append(e)

result = []
for start in range(1, n + 1):
    visited = [0] * (n + 1)
    result.append(bfs(start))

max_val = max(result)
ans = []
for i, val in enumerate(result):
    if val == max_val:
        ans.append(i + 1)
print(*ans)