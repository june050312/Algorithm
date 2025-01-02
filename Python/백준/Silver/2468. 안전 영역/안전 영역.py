import sys
input = sys.stdin.readline

def bfs(si, sj):
    q = []

    q.append([si, sj])
    visited[si][sj] = 1

    while q:
        ci, cj = q.pop(0)

        for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            ni, nj = ci + di, cj + dj

            if 0 <= ni < n and 0 <= nj < n and m[ni][nj] > rain and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                q.append([ni, nj])

n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]

ans = [0] * 100
for rain in range(100):
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if m[i][j] > rain and visited[i][j] == 0:
                bfs(i, j)
                ans[rain] += 1

print(max(ans))