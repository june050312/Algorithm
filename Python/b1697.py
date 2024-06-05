import sys
input = sys.stdin.readline

def bfs(start):
    q = []
    v = [0] * 100001

    q.append(start)
    v[start] = 1

    while q:
        c = q.pop(0)

        if c == sister_loc:
            return v[c] - 1

        for n in [c+1, c-1, c*2]:
            if 0 <= n <= 100000 and v[n] == 0:
                q.append(n)
                v[n] = v[c] + 1

subin_loc, sister_loc = map(int, input().split())

print(bfs(subin_loc))