import sys

input = sys.stdin.readline

k = []
for _ in range(9):
    k.append(int(input()))

over = sum(k) - 100

flag = False
for i in range(9):
    for j in range(i + 1, 9):
        if k[i] + k[j] == over:
            k[i] = k[j] = 0
            flag = True
            break
    if flag:
        break
    
k.sort()
for i in k[2:]:
    print(i)