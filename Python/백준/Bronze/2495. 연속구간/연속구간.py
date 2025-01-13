import sys

input = sys.stdin.readline

for _ in range(3):
    i = input().strip()
    ans = []
    cnt = 1
    for j in range(len(i) - 1):
        if i[j] == i[j+1]:
            cnt += 1
        else:
            ans.append(cnt)
            cnt = 1
    ans.append(cnt)
    print(max(ans))