import sys
n = int(sys.stdin.readline())
cnt = [0 for _ in range(10000)]
for _ in range(n):
    num = int(sys.stdin.readline())
    cnt[num - 1] += 1
for i in range(len(cnt)):
    if cnt[i] != 0:
        for _ in range(cnt[i]):
            print(i + 1)