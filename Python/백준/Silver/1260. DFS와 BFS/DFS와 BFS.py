import sys
input = sys.stdin.readline

def dfs(cur):
    dfsAns.append(cur)  # 방문 노드 추가
    visited[cur] = 1    # 방문 표시

    for next in adj[cur]:
        if not visited[next]:   # 방문하지 않은 노드인 경우
            dfs(next)

def bfs(init):
    q = []

    q.append(init)  # 큐에 초기 데이터 삽입
    bfsAns.append(init)
    visited[init] = 1

    while q:
        cur = q.pop(0)
        for next in adj[cur]:
            if not visited[next]:   # 방문하지 않은 노드 => 큐 삽입
                q.append(next)
                bfsAns.append(next)
                visited[next] = 1

n, m, start = map(int, input().split())

# 양방향 관계 리스트 제작
# 양방향으로 제작하는 이유는 노드에 들어올 때의 인덱스 나갈 때의 인덱스를 만들기 위해 제작
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

# 관계 리스트 내부 오름차순 정렬
for i in range(1, n + 1):
    adj[i].sort()

visited = [0] * (n + 1)
dfsAns = []
dfs(start)

visited = [0] * (n + 1)
bfsAns = []
bfs(start)

print(*dfsAns)
print(*bfsAns)