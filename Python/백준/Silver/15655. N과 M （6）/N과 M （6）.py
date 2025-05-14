import sys

input = sys.stdin.readline

def combination(depth, idx):
    if depth == n:
        for i in range(n):
            print(result[i], end = " ")
        print()
        return
    
    for i in range(idx, m):
            result[depth] = arr[i]
            combination(depth + 1, i + 1)

m, n = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

result = [0 for _ in range(n)]

combination(0, 0)