import sys

input = sys.stdin.readline

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

def lcm(a, b):
    return maxYear1 * maxYear2 / gcd(a, b)

for _ in range(int(input())):
    maxYear1, maxYear2, targetYear1, targetYear2 = map(int, input().split())
    year2 = targetYear1
    maxYear = lcm(maxYear1, maxYear2)
    while year2 <= maxYear:
        if (year2 - 1) % maxYear2 + 1 == targetYear2:
            break
        year2 += maxYear1
    if year2 > maxYear:
        print(-1)
    else:
        print(year2)