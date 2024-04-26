import sys

check = [0] * 1000000
check[0] = 1
check[1] = 1

for i in range(2, 1000000):
    if check[i] == 0:
        for j in range(2*i, 1000000, i):
            check[j] = 1

cnt = 0
start, end = map(int, sys.stdin.readline().strip().split())
for i in check[start : end + 1]:
    if i == 0:
        print(cnt + start)
    cnt += 1