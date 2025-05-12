import sys

input = sys.stdin.readline

def permutation(depth):
    if depth == n:
        for i in range(n):
            print(result[i], end = " ")
        print()
        return
    
    for i in range(m):
        if not v[i]:
            v[i] = 1
            result[depth] = arr[i]
            permutation(depth + 1)
            v[i] = 0

m, n = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

v = [0 for _ in range(m)]
result = [0 for _ in range(n)]

permutation(0)