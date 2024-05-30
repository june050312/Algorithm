import sys
input = sys.stdin.readline

def bfs(town, si, sj):
    unitCnt = 1
    q = []

    q.append([si, sj])
    town[si][sj] = 0

    while q:
        ci, cj = q.pop(0)
        
        for mi, mj in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
            ni, nj = ci + mi, cj + mj
            if 0 <= ni < n and 0 <= nj < n and town[ni][nj] == 1:
                unitCnt += 1
                q.append([ni, nj])
                town[ni][nj] = 0

    return unitCnt

n = int(input())

town = [list(map(int, input().strip())) for _ in range(n)]

cnt = []
for i in range(n):
    for j in range(n):
        if town[i][j] == 1:
            cnt.append(bfs(town, i, j))

cnt.sort()
print(len(cnt))
for i in cnt:
    print(i)