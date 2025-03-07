import sys, itertools

input = sys.stdin.readline

n, r = map(int, input().split())
arr = [i + 1 for i in range(n)]

perm = list(itertools.combinations(arr, r))
perm.sort(key=lambda perm : perm[0])
for i in perm:
    print(*i)
