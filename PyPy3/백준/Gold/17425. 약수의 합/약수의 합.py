import sys

input = sys.stdin.readline

MAX = 1000000

divisorsSum = [1] * (MAX + 1)

for i in range(2, MAX + 1):
    for j in range(i, MAX + 1, i):
        divisorsSum[j] += i
    divisorsSum[i] += divisorsSum[i - 1]

t = int(input())

for _ in range(t):
    n = int(input())
    print(divisorsSum[n])