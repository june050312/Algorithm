import sys

input = sys.stdin.readline

def aliquot(n, k):
    result = 0
    base = k

    while base <= n:
        result += n // base
        base *= k

    return result

n, m = map(int, input().split())

twoAliquot = aliquot(n, 2) - aliquot(m, 2) - aliquot(n-m, 2)
fiveAliquot = aliquot(n, 5) - aliquot(m, 5) - aliquot(n-m, 5)

print(min(twoAliquot, fiveAliquot))