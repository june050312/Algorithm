import sys

primeList = []
for i in range(2, 1000000):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        primeList.append(i)

for i in range(int(sys.stdin.readline().strip())):
    cnt = 0
    check = []
    n = int(sys.stdin.readline().strip())
    for j in primeList:
        if j >= n:
            break
        if n - j in primeList and n - j != 1 and j not in check:
            cnt += 1
            check.append(n - j)
    print(cnt)