import sys

checkList = [0] * 1000001
checkList[0] = 1
checkList[1] = 1

primeList = []

for i in range(2, 1000001):
    if checkList[i] == 0:
        primeList.append(i)
        for j in range(2*i, 1000001, i):
            checkList[j] = 1

for _ in range(int(sys.stdin.readline().strip())):
    cnt = 0
    num = int(sys.stdin.readline().strip())
    for i in primeList:
        if i >= num:
            break
        if not checkList[num - i] and i <= num - i:
            cnt += 1
    print(cnt)