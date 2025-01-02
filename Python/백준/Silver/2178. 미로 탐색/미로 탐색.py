import sys
input = sys.stdin.readline

def bfs(si, sj, ei, ej):
    q = []
    v = [[0] * M for _ in range(N)]

    # 여기는 어차피 [0, 0] 이라서 삽입부 이상해도 상관 X
    q.append([si, sj])
    v[si][sj] = 1

    # 큐 빌 때까지 반복
    while q:
        ci, cj = q.pop(0)

        if [ci, cj] == [ei, ej]:
            return v[ei][ej]

        for mi, mj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            ni, nj = ci + mi, cj + mj
            if 0 <= ni < N and 0 <= nj < M and maze[ni][nj] == 1 and v[ni][nj] == 0:
                q.append([ni, nj])
                v[ni][nj] = v[ci][cj] + 1

N, M = map(int, input().strip().split())
maze = [list(map(int, input().strip())) for _ in range(N)]

print(bfs(0, 0, N-1, M-1))