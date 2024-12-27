amount = int(input())
num = list(map(int, input().split()))
cnt = 0
for i in range(amount):
    num_cnt = 0
    for j in range(num[i]):
        if num[i] % (j + 1) == 0:
            num_cnt += 1
    if num_cnt == 2:
        cnt += 1
print(cnt)