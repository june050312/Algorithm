import sys

input = sys.stdin.readline

def permutation(depth):
    if depth == r:
        for i in range(r):
            print(result[i], end=" ")
        print()
        return
    
    for i in range(n):
        result[depth] = init[i]
        permutation(depth+1)

n, r = map(int, input().split())

init = [i + 1 for i in range(n)]
result = [0 for _ in range(n)]

permutation(0)